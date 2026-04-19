# Question 1: Name and Age
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old!")

# Question 2: Rectangle Area
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
print(f"The area is: {area}")

# Question 3: Temperature Conversion
celsius = float(input("Enter temp in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")

input("\nDone! Press Enter to exit...")