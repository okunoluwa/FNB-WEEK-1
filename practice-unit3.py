# calculator.py

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate basic operations
addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

# Display calculator results
print("\n" + "=" * 35)
print(f"{'CALCULATOR RESULTS':^35}")
print("=" * 35)

print(f"{'Addition:':<20} {addition:>10.2f}")
print(f"{'Subtraction:':<20} {subtraction:>10.2f}")
print(f"{'Multiplication:':<20} {multiplication:>10.2f}")

# Handle division by zero
if num2 == 0:
    print(f"{'Division:':<20} Cannot divide by zero")
    print(f"{'Floor Division:':<20} Cannot divide by zero")
    print(f"{'Modulus:':<20} Cannot divide by zero")
else:
    division = round(num1 / num2, 2)
    floor_division = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)

    print(f"{'Division:':<20} {division:>10.2f}")
    print(f"{'Floor Division:':<20} {floor_division:>10.2f}")
    print(f"{'Modulus:':<20} {modulus:>10.2f}")

print("=" * 35)