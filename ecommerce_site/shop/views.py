from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponse

from .models import Product, Cart, Order, OrderItem
from .forms import ProductForm, CheckoutForm


# ------------------- ADMIN CHECK -------------------
def is_admin(user):
    return user.is_superuser


# ------------------- PUBLIC VIEWS -------------------
def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, 'Account created successfully!')
        return redirect('home')

    return render(request, 'shop/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')

    return render(request, 'shop/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')


# ------------------- CART -------------------
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f'{product.name} added to cart!')
    return redirect('home')


@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.get_total() for item in cart_items)
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})


@login_required
def update_cart(request, cart_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
        quantity = int(request.POST.get('quantity', 1))

        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated!')
        else:
            cart_item.delete()
            messages.success(request, 'Item removed from cart!')

    return redirect('cart')


@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart!')
    return redirect('cart')


# ------------------- CHECKOUT -------------------
@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items.exists():
        messages.error(request, 'Your cart is empty!')
        return redirect('cart')

    total = sum(item.get_total() for item in cart_items)

    if request.method == 'POST':
        form = CheckoutForm(request.POST, request.FILES)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                customer_name=form.cleaned_data['customer_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                total_amount=total,
                payment_screenshot=form.cleaned_data['payment_screenshot']
            )

            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )

            cart_items.delete()
            messages.success(request, 'Order placed successfully!')
            return redirect('order_success', order_id=order.id)
    else:
        form = CheckoutForm(initial={
            'customer_name': request.user.get_full_name() or request.user.username,
            'email': request.user.email
        })

    return render(request, 'shop/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'total': total
    })


@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'shop/order_success.html', {'order': order})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'shop/my_orders.html', {'orders': orders})


# ------------------- ADMIN -------------------
@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    context = {
        'total_products': Product.objects.count(),
        'total_orders': Order.objects.count(),
        'pending_orders': Order.objects.filter(status='pending').count(),
        'total_revenue': Order.objects.aggregate(total=Sum('total_amount'))['total'] or 0,
        'recent_orders': Order.objects.all()[:10],
    }
    return render(request, 'shop/admin_dashboard.html', context)


@login_required
@user_passes_test(is_admin)
def admin_products(request):
    products = Product.objects.all()
    return render(request, 'shop/admin_products.html', {'products': products})


@login_required
@user_passes_test(is_admin)
def admin_add_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Product added successfully!')
        return redirect('admin_products')

    return render(request, 'shop/admin_product_form.html', {'form': form, 'title': 'Add Product'})


@login_required
@user_passes_test(is_admin)
def admin_edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if form.is_valid():
        form.save()
        messages.success(request, 'Product updated successfully!')
        return redirect('admin_products')

    return render(request, 'shop/admin_product_form.html', {'form': form, 'title': 'Edit Product'})


@login_required
@user_passes_test(is_admin)
def admin_delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('admin_products')


@login_required
@user_passes_test(is_admin)
def admin_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'shop/admin_orders.html', {'orders': orders})


@login_required
@user_passes_test(is_admin)
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        order.status = request.POST.get("status")
        order.save()
        messages.success(request, 'Order status updated!')
        return redirect('admin_order_detail', order_id=order.id)

    return render(request, 'shop/admin_order_detail.html', {'order': order})

def order_detail(request, id):
    return HttpResponse(f"Order Detail Page for Order ID: {id}")    