# secure_password_hint.py

# Ask the user to enter their password
password = input("Enter your password: ")

# Remove accidental spaces at the beginning and end
password = password.strip()

# Get the first and last characters
first_letter = password[0]
last_letter = password[-1]

# Display the hint using an f-string and uppercase letters
print(f"Your password hint: It starts with {first_letter.upper()} and ends with {last_letter.upper()}")