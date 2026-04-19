try:
    print("--- Number Comparison ---")
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    if n1 > n2:
        print(f"{n1} is greater.")
    elif n1 < n2:
        print(f"{n2} is greater.")
    else:
        print("They are equal.")

    print("\n--- Discount Eligibility ---")
    age = int(input("Enter age: "))
    card = input("Student card? (yes/no): ").strip().lower()

    if age < 18 or card == "yes":
        print("Result: You get a discount!")
    else:
        print("Result: Full price.")
except ValueError:
    print("Error: Please use numbers for age and comparisons.")

input("\nDone! Press Enter to exit...")