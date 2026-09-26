# Simple To-Do List Manager

# Start with three tasks
tasks = ["Buy groceries", "Finish homework", "Call the dentist"]

# Display the current to-do list
print("========================================")
print("         My To-Do List")
print("========================================")

print(f"1. {tasks[0]}")
print(f"2. {tasks[1]}")
print(f"3. {tasks[2]}")

print()
print(f"Total tasks: {len(tasks)}")

# Ask the user what they want to do
print()
print("What would you like to do?")
print("1. Add a task")
print("2. Remove a task")

choice = input("Choice: ")

# Add a new task
if choice == "1":
    new_task = input("Enter new task: ")
    tasks.append(new_task)

    print()
    print("Updated list:")

    # Display all tasks with numbers starting at 1
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print()
    print(f"Total tasks: {len(tasks)}")

# Remove a task
elif choice == "2":
    try:
        task_number = int(input("Enter task number to remove: "))

        # Make sure the number is actually in the list
        if task_number < 1 or task_number > len(tasks):
            raise IndexError

        # User sees numbers starting at 1,
        # but Python list indexes start at 0
        removed_task = tasks.pop(task_number - 1)

        print(f"Removed: {removed_task}")

        print()
        print("Updated list:")

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

        print()
        print(f"Total tasks: {len(tasks)}")

    except (ValueError, IndexError):
        print("That's not a valid task number.")

# Handle invalid menu choices
else:
    print("Invalid choice. Please enter 1 or 2.")