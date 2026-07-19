# student_info.py

# Collect user information
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

# Create full name
full_name = first_name + " " + surname

# Greeting
print(f"\nWelcome, {full_name}!")

# Display name in different formats
print(f"Name in UPPERCASE: {full_name.upper()}")
print(f"Name in Title Case: {full_name.title()}")

# Calculate age in months
age_in_months = age * 12
print(f"Age in months: {age_in_months}")

# Round favourite number
rounded_number = round(favourite_number, 2)
print(f"Favourite number (rounded): {rounded_number}")

# Display data types
print("\nData Types:")
print(f"First Name: {type(first_name)}")
print(f"Surname: {type(surname)}")
print(f"Age: {type(age)}")
print(f"Favourite Number: {type(favourite_name)}")