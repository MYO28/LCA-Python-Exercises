# Question 1: Creating and Modifying Lists
# Create a list of fruits
fruits = ["apple", "banana", "cherry"]

# Add a fruit to the end of the list
fruits.append("orange")

# Insert a fruit at the beginning of the list
fruits.insert(0, "grape")

#Remove a fruit from the list
fruits.remove("banana")

# Print the modified list of fruits
print(fruits)

# Question 2: List Operations
# Create a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]

# Create a new list with each number squared
squared_numbers = [num ** 2 for num in numbers]
# Find the sum and average of the original numbers
total_sum = sum(numbers)
average = total_sum / len(numbers)

# Print the results
print("Squared Numbers:", squared_numbers)
print("Sum:", total_sum)
print("Average:", average)

# Question 3: Creating and Modifying Dictionaries
# Create a dictionary of countries and their capitals
countries = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}
# Add a new country-capital pair to the dictionary
countries["Germany"] = "Berlin"
# Update the capital of an existing country
countries["France"] = "Lyon"

# Remove a country from the dictionary
del countries["USA"]

# Print the modified dictionary of countries and capitals
print(countries)  

# Question 4: Dictionary Operations
# Create a dictionary of fruits and their colors
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red"
}
# Print all the fruits (keys) in the dictionary
print("Fruits:", list(fruit_colors.keys()))

# Print all the colors (values) in the dictionary
print("Colors:", list(fruit_colors.values()))

# Print each fruit and its corresponding color
for fruit, color in fruit_colors.items():
    print(f"{fruit}: {color}")

# Check if a fruit is in the dictionary and print its color
fruit_to_check = "banana"
if fruit_to_check in fruit_colors:
    print(f"The color of the {fruit_to_check} is {fruit_colors[fruit_to_check]}.")
else:
    print(f"{fruit_to_check} is not in the dictionary.")
