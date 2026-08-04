task = ["😍"]

print("1. Add Task")
print("2. View task")
print("3. Remove task")
print("4. Marks task as done")
print("5. Exit")

while True:
    user = input("Interact with menu: ").lower()

    if user not in ["1", "2", "3", "4", "5"]:
        print("Interaction menu has only (1-5) options.")
        continue

    if user == "1":
        add = input("Enter the task: ").lower()
        task.append(add)

    if user == "2":
        print(task)

    if user == "3":
        rem = input("Enter the task which you wanted to delete: ").lower()
        task.remove(rem)
    else:
        print("Task not found.")

    if user == "4":
        mark = int(input("Enter the task you wanted to mark it as completed: "))
        task[mark] += " ✅"
    else:
        print("Invalid task number.")

    if user == "5":
        print("Thanks for using our TO-DO-List")
        break