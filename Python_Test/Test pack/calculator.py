def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", num1 + num2)

            elif choice == '2':
                print(num1, "-", num2, "=", num1 - num2)

            elif choice == '3':
                print(num1, "*", num2, "=", num1 * num2)

            elif choice == '4':
                if num2 != 0:
                    print(num1, "/", num2, "=", num1 / num2)
                else:
                    print("Error! Division by zero is not allowed.")
        elif choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

calculator()