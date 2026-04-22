# Question 1: Basic Function Definition and Calling
# TODO: Define a function called 'greet' that prints "Hello, World!"
def greet():
    print("Hello, World!")

# TODO: Call the 'greet' function
greet()


#------------------------------------------------------------------------------------
# Question 2: Function with Parameters
# TODO: Define a function called 'personalized_greeting' that takes a name as a parameter
def personalized_greeting(name):
    print(f"Hello, {name}!")

# TODO: Call the 'personalized_greeting' function using user input
user_name = input("Enter your name: ")
personalized_greeting(user_name)


#------------------------------------------------------------------------------------
# Question 3: Function with Return Value
# TODO: Define a function called 'square' that takes a number and returns its square
def square(number):
    return number * number

# TODO: Ask the user for a number, call the function, and print the result
# We use int() because input() always returns text (a string)
num_to_square = int(input("Enter a number to square: "))
result = square(num_to_square)
print(f"The square of {num_to_square} is: {result}")


#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value
# TODO: Define a function called 'rectangle_area' that returns the area
def rectangle_area(length, width):
    return length * width

# TODO: Call the function with user inputs and print the result
l = int(input("Enter the length of the rectangle: "))
w = int(input("Enter the width of the rectangle: "))
print(f"The area of the rectangle is: {rectangle_area(l, w)}")


#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument
# TODO: Define 'apply_operation' that takes a function and a number
def apply_operation(func, number):
    return func(number)

# TODO: Define a function called 'double' 
def double(number):
    return number * 2

# TODO: Use 'apply_operation' with 'double' and 7
print(f"Applying 'double' to 7: {apply_operation(double, 7)}")

# TODO: Use 'apply_operation' with 'square' and 3
print(f"Applying 'square' to 3: {apply_operation(square, 3)}")

input("\nPress Enter to exit...")