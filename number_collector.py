# Ask for the first number
try:
    number1 = int(input("Enter number 1: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    number1 = 0

# Ask for the second number
try:
    number2 = int(input("Enter number 2: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    number2 = 0

# Ask for the third number
try:
    number3 = int(input("Enter number 3: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    number3 = 0

# Calculate the sum
total = number1 + number2 + number3

# Calculate the average
average = total / 3

# Display the results
print()
print(f"Your numbers: {number1}, {number2}, {number3}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")