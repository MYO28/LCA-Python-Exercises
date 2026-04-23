# Question 1: Using a for loop with a list
# Create a list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]


# Use a for loop to print each fruit in the list
for fruit in fruits:
    print(fruit)


    # Question 2: Using a while loop for countdown

    # Use a while loop to create a countdown from 5 to 1  
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1


    # Question 3: Using a for loop with range()
    # Use a for loop to print the first 10 square numbers
for i in range(1, 11):
    print(i ** 2)


    # Question 4: Using the random module

    # Import the random module
import random
# Use the random module to generate a random number between 1 and 100
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

# Create a list of colors
colors = ["red", "blue", "green", "yellow", "purple"]
# Use the random module to select a random color from the list
random_color = random.choice(colors)
print(f"Randomly selected color: {random_color}")

# Use a for loop to select and print 3 random colors from the list
for _ in range(3):
    random_color = random.choice(colors)
    print(f"Randomly selected color: {random_color}")
