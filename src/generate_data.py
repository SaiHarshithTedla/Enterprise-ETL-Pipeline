from faker import Faker
import pandas as pd
import random
import os
from datetime import datetime, timedelta

# =====================================================
# Initialization
# =====================================================

fake = Faker("en_IN")
random.seed(42)

RAW_DATA_PATH = os.path.join("data", "raw")
os.makedirs(RAW_DATA_PATH, exist_ok=True)

CATEGORIES = [
    "Electronics",
    "Fashion",
    "Home & Kitchen",
    "Sports",
    "Books",
    "Grocery"
]

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery"
]

# =====================================================
# Customers
# =====================================================

def generate_customers(num_customers=5000):

    customers = []

    for customer_id in range(1, num_customers + 1):

        customers.append({
            "customer_id": customer_id,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "gender": random.choice(["Male", "Female"]),
            "city": fake.city(),
            "state": fake.state()
        })

    df = pd.DataFrame(customers)

    df.to_csv(
        os.path.join(RAW_DATA_PATH, "customers.csv"),
        index=False
    )

    print(f"✅ customers.csv created ({len(df)} records)")


# =====================================================
# Products
# =====================================================

def generate_products(num_products=500):

    products = []

    for product_id in range(1, num_products + 1):

        category = random.choice(CATEGORIES)

        products.append({
            "product_id": product_id,
            "product_name": f"{category} Product {product_id}",
            "category": category,
            "price": round(random.uniform(100, 50000), 2)
        })

    df = pd.DataFrame(products)

    df.to_csv(
        os.path.join(RAW_DATA_PATH, "products.csv"),
        index=False
    )

    print(f"✅ products.csv created ({len(df)} records)")


# =====================================================
# Orders
# =====================================================

def generate_orders(num_orders=25000, num_customers=5000):

    orders = []

    start_date = datetime(2024, 1, 1)

    for order_id in range(1, num_orders + 1):

        order_date = start_date + timedelta(
            days=random.randint(0, 730)
        )

        orders.append({
            "order_id": order_id,
            "customer_id": random.randint(1, num_customers),
            "order_date": order_date.strftime("%Y-%m-%d"),
            "payment_method": random.choice(PAYMENT_METHODS)
        })

    df = pd.DataFrame(orders)

    df.to_csv(
        os.path.join(RAW_DATA_PATH, "orders.csv"),
        index=False
    )

    print(f"✅ orders.csv created ({len(df)} records)")


# =====================================================
# Order Items
# =====================================================

def generate_order_items(num_orders=25000, num_products=500):

    order_items = []

    order_item_id = 1

    for order_id in range(1, num_orders + 1):

        number_of_products = random.randint(1, 5)

        selected_products = random.sample(
            range(1, num_products + 1),
            number_of_products
        )

        for product_id in selected_products:

            order_items.append({
                "order_item_id": order_item_id,
                "order_id": order_id,
                "product_id": product_id,
                "quantity": random.randint(1, 5)
            })

            order_item_id += 1

    df = pd.DataFrame(order_items)

    df.to_csv(
        os.path.join(RAW_DATA_PATH, "order_items.csv"),
        index=False
    )

    print(f"✅ order_items.csv created ({len(df)} records)")


# =====================================================
# Main
# =====================================================

def main():

    print("=" * 60)
    print("RetailX Enterprise Data Generator")
    print("=" * 60)

    generate_customers()
    generate_products()
    generate_orders()
    generate_order_items()

    print("\n🎉 All datasets generated successfully!")
    print(f"\nLocation: {RAW_DATA_PATH}")


if __name__ == "__main__":
    main()