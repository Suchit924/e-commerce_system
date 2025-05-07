from app import create_app, db
from app.models import Product

# Create the Flask app and initialize the database
app = create_app()

# Open an application context
with app.app_context():
    # Sample products to add with images
    products = [
        Product(name="T-shirt", price=2000, description="A stylish T-shirt.", image="product_images/tshirt.webp"),
        Product(name="Laptop", price=80000, description="A high-performance laptop.", image="product_images/laptop.webp"),
        Product(name="Headphones", price=15000, description="Noise-canceling headphones.", image="product_images/headphones.webp"),
        Product(name="Mug", price=500, description="A ceramic coffee mug.", image="product_images/mug.webp")
    ]

    # Add products to the database
    db.session.add_all(products)
    db.session.commit()

    print("Sample products with images added successfully!")
