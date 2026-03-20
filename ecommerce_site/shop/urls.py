from django.urls import path
from . import views

urlpatterns = [
    # Public pages
    path('order/<int:id>/', views.order_detail, name='order_detail'),
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Cart functionality
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:cart_id>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),

    # Checkout and orders
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/<int:order_id>/', views.order_success, name='order_success'),
    path('my-orders/', views.my_orders, name='my_orders'),

    # Admin panel
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # ✅ NEW
    path('dashboard/products/', views.admin_products, name='admin_products'),
    path('dashboard/products/add/', views.admin_add_product, name='admin_add_product'),
    path('dashboard/products/edit/<int:product_id>/', views.admin_edit_product, name='admin_edit_product'),
    path('dashboard/products/delete/<int:product_id>/', views.admin_delete_product, name='admin_delete_product'),

    path('dashboard/orders/', views.admin_orders, name='admin_orders'),
    path('dashboard/orders/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
]
