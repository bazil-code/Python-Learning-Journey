def calculator():
    print("Welcome to the Python Calculator!")
    print("Select the operation you'd like to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get user input for operation
    choice = input("Enter the number corresponding to your choice (1/2/3/4): ")
    
    # Validate user input
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please run the program again and select a valid option.")
        return
    
    try:
        # Get numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Perform the selected operation
    if choice == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif choice == '4':
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()
