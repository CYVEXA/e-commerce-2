# Quick Start Guide - ShopEase

## 🚀 Get Started in 5 Minutes

### Option 1: Automated Setup (Recommended)

```bash
# Make setup script executable
chmod +x setup.sh

# Run setup script
./setup.sh
```

The script will:
- Create virtual environment
- Install all dependencies
- Set up database
- Create media directories
- Ask you to create an admin account

### Option 2: Manual Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create directories
mkdir -p media/products media/payment_proofs static

# 3. Run migrations
python manage.py makemigrations
python manage.py migrate

# 4. Create admin account
python manage.py createsuperuser

# 5. Start server
python manage.py runserver
```

## 📱 Access the Website

- **Main Website**: http://127.0.0.1:8000/
- **Admin Dashboard**: http://127.0.0.1:8000/admin-dashboard/
- **Django Admin**: http://127.0.0.1:8000/admin/

## 👤 First Steps

### As Admin:
1. Login with your superuser credentials
2. Click "Admin" in the navigation
3. Go to "Products" → "Add New Product"
4. Add at least one product with image

### As Customer:
1. Click "Sign Up" to create an account
2. Browse products on the homepage
3. Add products to cart
4. Proceed to checkout
5. Upload payment proof
6. Place order

## 🎨 Features Included

✅ User Registration & Login
✅ Product Catalog with Images
✅ Shopping Cart
✅ Checkout with Customer Details
✅ Payment QR Code
✅ Payment Proof Upload
✅ Order Management
✅ Admin Dashboard
✅ Product Management (Add/Edit/Delete)
✅ Order Tracking
✅ Responsive Mobile Design

## ⚙️ Configuration

### Update Payment Details

Edit `templates/shop/checkout.html` and replace:
- QR Code image (line ~100)
- UPI ID (currently: shopease@upi)
- Payment instructions

### Customize Theme

Edit `templates/base.html` CSS variables:
```css
--primary-color: #FF6B35;
--secondary-color: #004E89;
--accent-color: #F77F00;
```

## 📊 Database Schema

The application uses these main models:
- **Product**: name, description, price, image, stock
- **Cart**: user, product, quantity
- **Order**: customer details, total, payment proof, status
- **OrderItem**: order, product, quantity, price

## 🔒 Security Reminders

Before deploying to production:
- [ ] Change SECRET_KEY in settings.py
- [ ] Set DEBUG = False
- [ ] Update ALLOWED_HOSTS
- [ ] Use environment variables
- [ ] Set up proper database (PostgreSQL/MySQL)
- [ ] Configure HTTPS
- [ ] Set up proper static/media file serving

## 📞 Need Help?

Common issues:
- **Port already in use**: Try `python manage.py runserver 8001`
- **Images not showing**: Check media directories exist
- **Admin not accessible**: Create superuser account
- **Static files missing**: Run `python manage.py collectstatic`

## 📝 Sample Data

To test quickly, add some sample products:
1. Login as admin
2. Add products with these sample details:

**Product 1:**
- Name: Wireless Headphones
- Price: 2999
- Description: Premium quality wireless headphones with noise cancellation
- Stock: 50

**Product 2:**
- Name: Smart Watch
- Price: 4999
- Description: Fitness tracker with heart rate monitor
- Stock: 30

**Product 3:**
- Name: Laptop Backpack
- Price: 1499
- Description: Durable backpack with laptop compartment
- Stock: 100

## 🎯 What's Next?

After basic setup:
1. Customize the payment QR code
2. Add your real products
3. Test the complete checkout flow
4. Customize colors and branding
5. Add email notifications (optional)
6. Set up production hosting

## 💡 Tips

- Use high-quality product images (recommended: 800x800px)
- Keep product descriptions concise and clear
- Test mobile responsiveness on different devices
- Regularly check pending orders in admin panel
- Update order status after verifying payments

Happy Selling! 🎉
