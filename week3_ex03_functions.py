# ------------------------------------------------------------------------------------
# Question 1: Basic Function Definition and Calling

# TODO: Define a function called 'greet' that prints "Hello, World!"
def greet():
    print("Hello, World!")

# TODO: Call the 'greet' function
greet()


# ------------------------------------------------------------------------------------
# Question 2: Function with Parameters

# TODO: Define a function called 'personalized_greeting' that takes a name as a parameter
def personalized_greeting(name):
    print(f"Hello, {name}!")

# TODO: Call the 'personalized_greeting' function with your name
personalized_greeting("Yusuf")


# ------------------------------------------------------------------------------------
# Question 3: Function with Return Value

# TODO: Define a function called 'square' that takes a number and returns its square
def square(number):
    return number * number

# TODO: Call the 'square' function with the number 5 and print the result
result = square(5)
print(f"The square of 5 is: {result}")


# ------------------------------------------------------------------------------------
# Question 4: Multiple Parameters

# TODO: Define a function called 'calculate_area' (width * height)
def calculate_area(width, height):
    return width * height

# TODO: Call the function and print the area
area = calculate_area(10, 5)
print(f"The area of the rectangle is: {area}")

input("\nPress Enter to exit...")