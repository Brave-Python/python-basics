import json

products_json = '''
[
    {
        "id": "PROD-001",
        "name": "Wireless Mouse",
        "price": 24.99,
        "in_stock": true,
        "category": "Accessories",
        "brand": "Logitech",
        "rating": 4.5,
        "warranty_months": 12,
        "color": "Black"
    },
    {
        "id": "PROD-002",
        "name": "Mechanical Keyboard",
        "price": 89.99,
        "in_stock": false,
        "category": "Accessories",
        "brand": "Corsair",
        "rating": 4.8,
        "warranty_months": 24,
        "color": "RGB"
    },
    {
        "id": "PROD-003",
        "name": "USB-C Hub",
        "price": 34.99,
        "in_stock": true,
        "category": "Adapters",
        "brand": "Anker",
        "rating": 4.3,
        "warranty_months": 18,
        "color": "Gray"
    },
    {
        "id": "PROD-004",
        "name": "27-inch Monitor",
        "price": 299.99,
        "in_stock": true,
        "category": "Displays",
        "brand": "Dell",
        "rating": 4.6,
        "warranty_months": 36,
        "color": "Black",
        "resolution": "2560x1440",
        "refresh_rate": 144
    },
    {
        "id": "PROD-005",
        "name": "Wireless Headphones",
        "price": 149.99,
        "in_stock": true,
        "category": "Audio",
        "brand": "Sony",
        "rating": 4.7,
        "warranty_months": 12,
        "color": "Silver",
        "battery_hours": 30,
        "noise_cancelling": true
    },
    {
        "id": "PROD-006",
        "name": "External SSD 1TB",
        "price": 119.99,
        "in_stock": false,
        "category": "Storage",
        "brand": "Samsung",
        "rating": 4.9,
        "warranty_months": 60,
        "color": "Blue",
        "capacity_gb": 1000,
        "read_speed_mbps": 1050
    },
    {
        "id": "PROD-007",
        "name": "Webcam 1080p",
        "price": 69.99,
        "in_stock": true,
        "category": "Accessories",
        "brand": "Logitech",
        "rating": 4.4,
        "warranty_months": 24,
        "color": "Black",
        "resolution": "1920x1080",
        "framerate": 60
    },
    {
        "id": "PROD-008",
        "name": "Gaming Mouse Pad",
        "price": 19.99,
        "in_stock": true,
        "category": "Accessories",
        "brand": "Razer",
        "rating": 4.2,
        "warranty_months": 6,
        "color": "Black",
        "size_cm": "90x40"
    }
]
'''

products = json.loads(products_json)

print(f"Total products: {len(products)}")
print("=" * 70)

for product in products:
    status = "Available" if product["in_stock"] else "Out of stock"
    
    print(f"\n{product['name']} ({product['id']})")
    print(f"  Brand: {product['brand']}")
    print(f"  Category: {product['category']}")
    print(f"  Price: ${product['price']}")
    print(f"  Rating: {product['rating']}/5.0")
    print(f"  Warranty: {product['warranty_months']} months")
    print(f"  Color: {product['color']}")
    print(f"  Status: {status}")
    
  

print("\n" + "=" * 70)
print(f"\nIn Stock: {sum(1 for p in products if p['in_stock'])}")
print(f"Out of Stock: {sum(1 for p in products if not p['in_stock'])}")
print(f"Average Price: ${sum(p['price'] for p in products) / len(products):.2f}")
print(f"Average Rating: {sum(p['rating'] for p in products) / len(products):.2f}/5.0")


