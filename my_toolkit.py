# My Python Toolkit


def calculate_average(numbers):
    """Return the average of a list of numbers. Returns 0 if the list is empty."""
    if len(numbers) == 0:
        return 0

    total = sum(numbers)
    return total / len(numbers)


def find_max_and_min(numbers):
    """Return the maximum and minimum values as a tuple without using max() or min()."""
    if len(numbers) == 0:
        return (None, None)

    max_value = numbers[0]
    min_value = numbers[0]

    for number in numbers:
        if number > max_value:
            max_value = number

        if number < min_value:
            min_value = number

    return (max_value, min_value)


def count_occurrences(items, target):
    """Return the number of times the target value appears in a list."""
    count = 0

    for item in items:
        if item == target:
            count += 1

    return count


def is_palindrome(text):
    """Return True if text reads the same forward and backward, ignoring spaces and case."""
    cleaned_text = text.replace(" ", "").lower()

    return cleaned_text == cleaned_text[::-1]


def create_report(title, scores):
    """Return a formatted report containing the average, highest, and lowest scores."""
    average = calculate_average(scores)
    max_value, min_value = find_max_and_min(scores)

    if len(scores) == 0:
        report = (
            f"=== {title} ===\n"
            f"Total Scores: 0\n"
            f"Average: 0\n"
            f"Highest: None\n"
            f"Lowest: None"
        )
    else:
        report = (
            f"=== {title} ===\n"
            f"Total Scores: {len(scores)}\n"
            f"Average: {average:.2f}\n"
            f"Highest: {max_value}\n"
            f"Lowest: {min_value}"
        )

    return report


# Test section
if __name__ == "__main__":
    # Required tests
    test_scores = [85, 92, 78, 95, 88, 70, 93]

    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))

    # Edge case tests
    print()
    print("=== Edge Case Tests ===")

    # Empty lists
    print(f"Average of empty list: {calculate_average([])}")
    print(f"Max/Min of empty list: {find_max_and_min([])}")

    # Target appears multiple times
    repeated_items = [1, 2, 2, 3, 2, 4]
    print(f"Count of 2: {count_occurrences(repeated_items, 2)}")

    # Target does not appear
    print(f"Count of 10: {count_occurrences(repeated_items, 10)}")

    # Palindrome phrase with spaces
    phrase = "A man a plan a canal Panama"
    print(f"Phrase palindrome: {is_palindrome(phrase)}")

    # Single character
    print(f"'A' palindrome: {is_palindrome('A')}")

    # Mixed case
    print(f"'RaceCar' palindrome: {is_palindrome('RaceCar')}")

    # Empty report
    print()
    print(create_report("Empty Scores", []))