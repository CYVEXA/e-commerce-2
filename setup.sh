#!/bin/bash

echo "=========================================="
echo "ShopEase E-Commerce Website Setup"
echo "=========================================="
echo ""

# Step 1: Create virtual environment
echo "Step 1: Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Step 2: Install dependencies
echo "Step 2: Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 3: Create necessary directories
echo "Step 3: Creating media directories..."
mkdir -p media/products
mkdir -p media/payment_proofs
mkdir -p static

# Step 4: Run migrations
echo "Step 4: Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Step 5: Create superuser
echo ""
echo "Step 5: Creating admin superuser..."
echo "Please enter admin credentials:"
python manage.py createsuperuser

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "To start the server:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Run server: python manage.py runserver"
echo ""
echo "Then visit: http://127.0.0.1:8000/"
echo ""
echo "Admin Panel: http://127.0.0.1:8000/admin-dashboard/"
echo "=========================================="
