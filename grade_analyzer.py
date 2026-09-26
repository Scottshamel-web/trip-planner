# Grade Analyzer

# Starting list of student scores
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

# Grade counters
a_count = 0
b_count = 0
c_count = 0
d_count = 0
f_count = 0

# Use a for loop to categorize each score
for score in scores:
    if score >= 90:
        a_count += 1
    elif score >= 80:
        b_count += 1
    elif score >= 70:
        c_count += 1
    elif score >= 60:
        d_count += 1
    else:
        f_count += 1

# Calculate score information
total_scores = len(scores)
average = sum(scores) / total_scores
highest = max(scores)
lowest = min(scores)

passing = 0
failing = 0

# Count passing and failing scores
for score in scores:
    if score >= 60:
        passing += 1
    else:
        failing += 1

# Calculate percentages
passing_percent = (passing / total_scores) * 100
failing_percent = (failing / total_scores) * 100

# Display grade analysis
print("=== Grade Analyzer ===")
print(f"Total scores: {total_scores}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Passing: {passing} ({passing_percent:.1f}%)")
print(f"Failing: {failing} ({failing_percent:.1f}%)")

print()
print("Grade Distribution:")
print(f"A: {a_count} students")
print(f"B: {b_count} students")
print(f"C: {c_count} students")
print(f"D: {d_count} students")
print(f"F: {f_count} students")

# Allow the user to enter additional scores
print()
print("--- Add More Scores ---")

while True:
    user_input = input("Enter a score (or 'done' to finish): ")

    # Stop the loop when the user types done
    if user_input.lower() == "done":
        break

    try:
        new_score = int(user_input)

        # Make sure the score is between 0 and 100
        if new_score < 0 or new_score > 100:
            print("Please enter a score between 0 and 100.")
            continue

        # Add the score to the list
        scores.append(new_score)

        # Calculate and display the new average
        updated_average = sum(scores) / len(scores)
        print(f"Updated average: {updated_average:.1f}")

    except ValueError:
        print("Please enter a valid number or type 'done'.")

# Display final average
final_average = sum(scores) / len(scores)

print()
print(f"Final average: {final_average:.1f}")