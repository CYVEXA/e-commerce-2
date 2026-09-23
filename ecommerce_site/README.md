# ShopEase - E-Commerce Website

A modern, responsive e-commerce website built with Django, Bootstrap, and SQLite.

## Features

### Customer Features
- **User Authentication**: Login and signup functionality
- **Product Browsing**: View all products with images, names, and prices
- **Shopping Cart**: Add products to cart, update quantities, remove items
- **Checkout**: Complete order with customer details
- **Online Payment**: QR code payment integration
- **Payment Proof Upload**: Upload payment screenshots
- **Order History**: View all past orders and their status

### Admin Features
- **Dashboard**: Overview of products, orders, and revenue
- **Product Management**: Add, edit, and delete products
- **Order Management**: View all orders with customer details
- **Payment Verification**: View uploaded payment screenshots
- **Order Status Updates**: Update order status (Pending, Confirmed, Shipped, Delivered, Cancelled)

## Tech Stack

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, Bootstrap 5.3
- **Database**: SQLite3
- **Image Handling**: Pillow

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account:
- Username: (choose a username)
- Email: (your email)
- Password: (choose a strong password)

### Step 4: Create Required Directories

```bash
mkdir -p media/products media/payment_proofs
mkdir -p static
```

### Step 5: Run the Development Server

```bash
python manage.py runserver
```

The website will be accessible at: `http://127.0.0.1:8000/`

## Usage

### For Customers

1. **Sign Up**: Create an account at `/signup/`
2. **Browse Products**: View products on the homepage
3. **Add to Cart**: Click "Add to Cart" on products you want to buy
4. **Checkout**: 
   - Go to cart and click "Proceed to Checkout"
   - Fill in your details (name, email, phone, address)
   - Scan the QR code and make payment
   - Upload payment screenshot
   - Submit order
5. **View Orders**: Check your order history at "My Orders"

### For Admin

1. **Login**: Use the superuser credentials you created
2. **Access Admin Panel**: Click "Admin" in the navigation menu
3. **Add Products**:
   - Go to "Products" → "Add New Product"
   - Fill in product details (name, description, price, stock, image)
   - Click "Save Product"
4. **Manage Orders**:
   - Go to "Orders" to view all customer orders
   - Click "View" to see order details
   - View payment screenshots
   - Update order status

## Project Structure

```
ecommerce_site/
├── ecommerce_project/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── shop/                       # Main application
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── forms.py               # Django forms
│   ├── urls.py                # URL routing
│   ├── admin.py               # Admin configuration
│   └── context_processors.py # Cart count processor
├── templates/                  # HTML templates
│   ├── base.html
│   └── shop/
│       ├── home.html
│       ├── login.html
│       ├── signup.html
│       ├── cart.html
│       ├── checkout.html
│       ├── order_success.html
│       ├── my_orders.html
│       ├── admin_dashboard.html
│       ├── admin_products.html
│       ├── admin_product_form.html
│       ├── admin_orders.html
│       └── admin_order_detail.html
├── media/                      # Uploaded files
│   ├── products/              # Product images
│   └── payment_proofs/        # Payment screenshots
├── static/                     # Static files
├── manage.py                   # Django management script
└── requirements.txt            # Python dependencies
```

## Database Models

### Product
- Name, description, price
- Image upload
- Stock quantity
- Timestamps

### Cart
- User reference
- Product reference
- Quantity

### Order
- Customer details (name, email, phone, address)
- Total amount
- Payment screenshot
- Order status
- Timestamps

### OrderItem
- Order reference
- Product reference
- Quantity and price

## Payment Integration

The checkout page displays a QR code for payment. Update the QR code and payment details in:
- File: `templates/shop/checkout.html`
- Replace the placeholder QR code SVG with your actual payment QR code
- Update UPI ID or payment details

## Customization

### Change Colors/Theme
Edit the CSS variables in `templates/base.html`:
```css
:root {
    --primary-color: #FF6B35;
    --secondary-color: #004E89;
    --accent-color: #F77F00;
    --dark: #1A1A2E;
    --light: #F8F9FA;
    --success: #06D6A0;
}
```

### Add More Products
1. Login as admin
2. Go to Admin Panel → Products → Add New Product
3. Fill in all details and upload an image
4. Click "Save Product"

## Security Notes

**Important for Production:**
1. Change `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Update `ALLOWED_HOSTS` with your domain
4. Use environment variables for sensitive data
5. Use a production database (PostgreSQL, MySQL)
6. Set up proper media file serving
7. Enable HTTPS
8. Configure CSRF and security middleware properly

## Troubleshooting

### Images not displaying
- Make sure media directories exist
- Check `MEDIA_URL` and `MEDIA_ROOT` in settings.py
- Ensure you're running the development server

### Cart count not showing
- Verify `context_processors.py` is in TEMPLATES settings
- Check if user is logged in

### Admin panel not accessible
- Create superuser: `python manage.py createsuperuser`
- Login with superuser credentials

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please refer to Django documentation:
- https://docs.djangoproject.com/
- https://getbootstrap.com/docs/

## Credits

- Built with Django Framework
- Styled with Bootstrap 5
- Icons from Bootstrap Icons
- Fonts from Google Fonts (Outfit, Space Mono)
