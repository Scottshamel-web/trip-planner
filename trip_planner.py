# Road Trip Budget Planner

# Ask the user for trip information
destination = input("Enter your destination: ")

distance = float(input("Enter total distance in miles: "))
mpg = float(input("Enter your car's MPG: "))
gas_price = float(input("Enter current gas price per gallon: "))

nights = int(input("Enter number of nights: "))
hotel_cost = float(input("Enter average hotel cost per night: "))
food_budget = float(input("Enter daily food budget: "))

# Calculate trip costs
gallons = distance / mpg
total_gas_cost = gallons * gas_price
total_hotel_cost = nights * hotel_cost

# There is one more travel day than the number of nights
days = nights + 1
total_food_cost = days * food_budget

# Add all costs together
grand_total = total_gas_cost + total_hotel_cost + total_food_cost

# Display trip summary
print()
print("=== Road Trip Budget Planner ===")
print()
print(f"Destination: {destination}")
print(f"Distance: {distance:.2f} miles")
print()
print("--- Cost Breakdown ---")
print(f"Gas ({gallons:.2f} gal @ ${gas_price:.2f}/gal): ${total_gas_cost:.2f}")
print(f"Hotel ({nights} nights @ ${hotel_cost:.2f}):     ${total_hotel_cost:.2f}")
print(f"Food ({days} days @ ${food_budget:.2f}):       ${total_food_cost:.2f}")
print("-----------------------------")
print(f"Estimated Total:              ${grand_total:.2f}")