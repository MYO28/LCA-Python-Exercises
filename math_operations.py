# Define the math operations functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"


# Main calculator code
def main():
    # Use the functions directly (same file)
    while True:
        print("Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is: {result}")
            print("\nOperation complete. Press Enter to continue...")
            input()
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is: {result}")
            print("\nOperation complete. Press Enter to continue...")
            input()
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is: {result}")
            print("\nOperation complete. Press Enter to continue...")
            input()
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is: {result}")
            print("\nOperation complete. Press Enter to continue...")
            input()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
