#Creata a to do list
to_do_list=["Buy Groceries","Clean the house","Pay bills"]

## Adding to task
to_do_list.append("Schedule meeting")
to_do_list.append("Go For a Run")

## Removing a completed task
to_do_list.remove("Clean the house")

## checking if a task is in the list
if "Pay bills" in to_do_list:
    print("Don't forgrt to pay the utility bills")

print("To Do List remaining")
for task in to_do_list:
    print(f"-{task}")


#Create a list to store and calculate average grades for students
#Organizing student grades
grades = [85, 92, 78, 90, 88]

# Adding a new grade
grades.append(95)

# Calculating the average grade
average_grade = sum(grades) / len(grades)
print(f"Average Grade: {average_grade:.2f}")

# Finding the highest and lowest grades
highest_grade = max(grades)
lowest_grade = min(grades)
print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")


#Use a list to manage inventory items in a store
# Managing an inventory
inventory = ["apples", "bananas", "oranges", "grapes"]

# Adding a new item
inventory.append("strawberries")

# Removing an item that is out of stock
inventory.remove("bananas")

# Checking if an item is in stock
item = "oranges"
if item in inventory:
    print(f"{item} are in stock.")
else:
    print(f"{item} are out of stock.")

# Printing the inventory
print("Inventory List:")
for item in inventory:
    print(f"- {item}")


# Use a list to collect and analyze user feedback.
# Collecting user feedback
feedback = ["Great service!", "Very satisfied", "Could be better", "Excellent experience"]

# Adding new feedback
feedback.append("Not happy with the service")

# Counting specific feedback
positive_feedback_count = sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower())
print(f"Positive Feedback Count: {positive_feedback_count}")

# Printing all feedback
print("User Feedback:")
for comment in feedback:
    print(f"- {comment}")
