# South African Fuel Cost Calculator

kilometers = float(input("How many kilometers do you want to drive? "))
petrol_price = float(input("Enter the current petrol price per liter (R): "))

# 1 liter is used for every 10 kilometers
liters_needed = kilometers / 10

# Calculate the total cost
total_cost = liters_needed * petrol_price

# Round the final cost to 2 decimal places
total_cost = round(total_cost, 2)

# Display the result
print(f"\nYou need {liters_needed} liters of fuel.")
print(f"Total fuel cost: R{total_cost}")