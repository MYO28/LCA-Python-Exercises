# Question 1: Arithmetic and Assignment Operators
x = 10
y = 5

# TODO: Add 3 to x using the += operator
x += 3 # [cite: 51]

# TODO: Multiply y by 2 using the *= operator
y *= 2 # [cite: 52]

# TODO: Divide x by y and store the result in a variable called 'result'
result = x / y # [cite: 47]

# TODO: Print the value of 'result'
print(f"Question 1 Result: {result}")

#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
a, b, c = 15, 10, 5

# TODO: Create a condition that checks if a is greater than b
cond1 = a > b #

# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
cond2 = (b % 2 == 0) # [cite: 47, 53]

# TODO: Create a condition that checks if c is less than or equal to a
cond3 = c <= a # [cite: 60]

# TODO: Combine using logical operators
# final_condition is True if: (a > b) OR (b is even AND c <= a)
final_condition = cond1 or (cond2 and cond3) # [cite: 61]

# TODO: Print the value of 'final_condition'
print(f"Question 2 Final Condition: {final_condition}")

#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask user for score
score = int(input("Enter test score (0-100): "))

# TODO: Implement grading system using if-elif-else
if score >= 90: # [cite: 17, 59]
    grade = "A"
elif score >= 80: # [cite: 20]
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else: # [cite: 21]
    grade = "F"

# TODO: Print the grade
print(f"Grade: {grade}")

#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Input two numbers
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

# TODO: Input operation
operation = input("Enter operation (+, -, *, /): ")

# TODO: Use conditional statements and handle division by zero
if operation == "+": # 
    calc_result = num1 + num2 # [cite: 47]
elif operation == "-":
    calc_result = num1 - num2
elif operation == "*":
    calc_result = num1 * num2
elif operation == "/":
    if num2 != 0: # [cite: 56]
        calc_result = num1 / num2
    else:
        calc_result = "Error: Division by zero"
else:
    calc_result = "Invalid operation"

# TODO: Print result
print(f"Operation Result: {calc_result}")