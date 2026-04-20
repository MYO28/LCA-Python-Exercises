# --- Exercise 02: Operators and Conditionals ---

# Question 1: Arithmetic and Assignment Operators
x = 10  # Initializing variables for the example
y = 5

x += 3        # Adds 3 to x (x is now 13)
y *= 2        # Multiplies y by 2 (y is now 10)
result = x / y 

print(f"Question 1 Result: {result}")

#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
a = 15
b = 4
c = 10

# Individual conditions
cond1 = a > b
cond2 = b % 2 == 0  # Modulus 2 equals 0 means it is even
cond3 = c <= a

# Combining conditions
# Logic: (A) OR (B AND C)
final_condition = cond1 or (cond2 and cond3)

print(f"Question 2 Final Condition: {final_condition}")

#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# We use int() because input() always returns a string
score = int(input("Enter a test score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    calc_result = num1 + num2
elif operation == "-":
    calc_result = num1 - num2
elif operation == "*":
    calc_result = num1 * num2
elif operation == "/":
    # Handling division by zero
    if num2 == 0:
        calc_result = "Error: Cannot divide by zero!"
    else:
        calc_result = num1 / num2
else:
    calc_result = "Invalid operation selected."

print(f"Result: {calc_result}")

# Keep the window open
input("\nPress Enter to exit...")