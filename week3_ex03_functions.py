# ------------------------------------------------------------------------------------
# Question 1: Basic Function
def greet():
    print("Hello, World!")

greet()

# ------------------------------------------------------------------------------------
# Question 2: Function with Parameters (Interactive)
def personalized_greeting(name):
    print(f"Hello, {name}!")

# TODO: Ask the user for their name first
user_name = input("Enter your name for a greeting: ")
personalized_greeting(user_name)

# ------------------------------------------------------------------------------------
# Question 3: Function with Return Value (Interactive)
def square(number):
    return number * number

# TODO: Ask the user for a number
user_num = int(input("Enter a number to square: "))
result = square(user_num)
print(f"The square of {user_num} is: {result}")

# ------------------------------------------------------------------------------------
# Question 4: Multiple Parameters (Interactive)
def calculate_area(width, height):
    return width * height

# TODO: Ask user for dimensions
w = int(input("Enter the rectangle width: "))
h = int(input("Enter the rectangle height: "))

area = calculate_area(w, h)
print(f"The area of the rectangle is: {area}")

input("\nPress Enter to exit...")