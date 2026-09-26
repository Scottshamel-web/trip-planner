# Product Inventory System

# Create the inventory dictionary
inventory = {
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "keyboard": {"price": 79.99, "quantity": 8},
    "monitor": {"price": 249.99, "quantity": 6}
}

# Display the inventory
print("==============================================")
print("              STORE INVENTORY")
print("==============================================")
print(f"{'Product':<12}{'Price':<12}{'Quantity':<10}")
print("----------------------------------------------")

for product, details in inventory.items():
    print(
        f"{product:<12}"
        f"${details['price']:<11.2f}"
        f"{details['quantity']:<10}"
    )

# Calculate total inventory value
total_value = 0

for product, details in inventory.items():
    product_value = details["price"] * details["quantity"]
    total_value += product_value

print("----------------------------------------------")
print(f"Total Inventory Value: ${total_value:.2f}")


# Let the user look up a product
print()
search_product = input("Enter a product to look up: ").lower()

product_info = inventory.get(search_product)

if product_info:
    print()
    print(f"Product: {search_product}")
    print(f"Price: ${product_info['price']:.2f}")
    print(f"Quantity: {product_info['quantity']}")
else:
    print("Product not found.")


# Let the user update a product quantity
print()
update_product = input("Enter a product to update: ").lower()

product_info = inventory.get(update_product)

if product_info:
    try:
        new_quantity = int(input("Enter the new quantity: "))
        inventory[update_product]["quantity"] = new_quantity

        print()
        print(f"{update_product} quantity updated to {new_quantity}.")
    except ValueError:
        print("Invalid quantity. Please enter a whole number.")
else:
    print("Product not found.")


# Track low-stock products using a set
low_stock = set()

for product, details in inventory.items():
    if details["quantity"] < 10:
        low_stock.add(product)


# Display the updated inventory
print()
print("==============================================")
print("            UPDATED INVENTORY")
print("==============================================")
print(f"{'Product':<12}{'Price':<12}{'Quantity':<10}")
print("----------------------------------------------")

for product, details in inventory.items():
    print(
        f"{product:<12}"
        f"${details['price']:<11.2f}"
        f"{details['quantity']:<10}"
    )


# Display low-stock alert
print()
print("Low Stock Alert:")

if low_stock:
    for product in low_stock:
        print(f"- {product}")
else:
    print("No products are low on stock.")