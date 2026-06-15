print("Simple Calculator")

while True:
    print("\nOptions:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Answer:", num1 + num2)

    elif choice == "2":
        print("Answer:", num1 - num2)

    elif choice == "3":
        print("Answer:", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Answer:", num1 / num2)

    else:
        print("Invalid choice!")
