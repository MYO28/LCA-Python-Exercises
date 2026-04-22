# ------------------------------------------------------------------------------------
# Question 1: Basic Function
def greet():
    print("Hello, World!")

greet()

# ------------------------------------------------------------------------------------
# Question 2: Function with Parameters
def personalized_greeting(name):
    print(f"Hello, {name}!")

# Use input() so the user can type their name
user_name = input("Enter your name: ")
personalized_greeting(user_name)

# ------------------------------------------------------------------------------------
# Question 3: Function with Return Value
def square(number):
    return number * number

# Convert the input to an integer (int) so we can do math
user_num = int(input("Enter a number to square: "))
result = square(user_num)
print(f"The square of {user_num} is: {result}")

# ------------------------------------------------------------------------------------
# Question 4: Multiple Parameters
def calculate_area(width, height):
    return width * height

# Get both dimensions from the user
w = int(input("Enter the rectangle width: "))
h = int(input("Enter the rectangle height: "))

area = calculate_area(w, h)
print(f"The area of the rectangle is: {area}")

input("\nPress Enter to exit...")