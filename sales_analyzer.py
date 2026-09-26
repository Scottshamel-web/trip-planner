import csv

# Dictionaries to store totals
product_revenue = {}
product_quantity = {}
daily_revenue = {}

total_revenue = 0

# Read the sales CSV file
with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        date = row["date"]
        product = row["product"]
        quantity = int(row["quantity"])
        price = float(row["price"])

        # Calculate revenue for this row
        revenue = quantity * price
        total_revenue += revenue

        # Track revenue by product
        if product not in product_revenue:
            product_revenue[product] = 0

        product_revenue[product] += revenue

        # Track quantity by product
        if product not in product_quantity:
            product_quantity[product] = 0

        product_quantity[product] += quantity

        # Track revenue by date
        if date not in daily_revenue:
            daily_revenue[date] = 0

        daily_revenue[date] += revenue


# Find the day with the highest revenue
highest_day = None
highest_day_revenue = 0

for date, revenue in daily_revenue.items():
    if revenue > highest_day_revenue:
        highest_day_revenue = revenue
        highest_day = date


# Write the text report
with open("sales_report.txt", "w") as report:
    report.write("=== Sales Report ===\n")
    report.write(f"Total Revenue: ${total_revenue:.2f}\n")

    report.write("\nRevenue by Product:\n")

    for product, revenue in product_revenue.items():
        report.write(f"{product}: ${revenue:.2f}\n")

    report.write("\nQuantity Sold by Product:\n")

    for product, quantity in product_quantity.items():
        report.write(f"{product}: {quantity}\n")

    report.write("\nHighest Revenue Day:\n")
    report.write(f"{highest_day}: ${highest_day_revenue:.2f}\n")


# Write product summary CSV
with open("product_summary.csv", "w", newline="") as file:
    fieldnames = ["product", "total_quantity", "total_revenue"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for product in product_revenue:
        writer.writerow({
            "product": product,
            "total_quantity": product_quantity[product],
            "total_revenue": f"{product_revenue[product]:.2f}"
        })


print("Sales analysis complete.")
print("Created sales_report.txt")
print("Created product_summary.csv")