def perform_operation(operation, num1, num2):
    """Performs the specified operation on two numbers."""
    operations = {
        'add': num1 + num2,
        'subtract': num1 - num2,
        'multiply': num1 * num2,
        'divide': num1 / num2 if num2 != 0 else 'undefined (division by zero)'
    }
    return operations.get(operation, "Invalid operation")

def show_menu():
    """Displays the calculator menu."""
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    """Main function to run the calculator."""
    while True:
        show_menu()
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Mali ka bro. Please enter a number between 1 and 5.")
            continue

        if choice == 5:
            print("Thank you for using my basic calculator. This is Ralph Goodbye!")
            break

        if choice not in range(1, 5):
            print("Wrong choice ka bro. Please select a valid option.")
            continue

        try:
            num1 = float(input("first number: "))
            num2 = float(input("second number: "))
        except ValueError:
            print("Invalid input ka bro. Please enter numeric values.")
            continue

        operation_map = {
            1: 'add',
            2: 'subtract',
            3: 'multiply',
            4: 'divide'
        }

        operation = operation_map.get(choice)
        result = perform_operation(operation, num1, num2)

        print(f"The result of the operation is: {result}")

if __name__ == "__main__":
    main()
