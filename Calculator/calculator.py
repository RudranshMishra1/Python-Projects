def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a/b


while True:
    print("\n==== Calculator ====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divition")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Thank you for using the calculator")
        break
 
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Please choose a valid option")
        continue

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter a number only")
        continue

    if choice == "1":
        result = add(num1,num2)
        print("Result:",result)

    if choice == "2":
        result = sub(num1,num2)
        print("Result:",result)

    if choice == "3":
        result = multi(num1,num2)
        print("Result:",result)

    if choice == "4":
        result = divide(num1,num2)
        print("Result:",result)