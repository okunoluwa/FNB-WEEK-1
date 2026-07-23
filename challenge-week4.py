# Smart ATM Withdrawal Simulator

# Set the bank balance
balance = 500

# Ask the user how much they want to withdraw
withdrawal = float(input("How much money do you want to withdraw? R"))

# Check the withdrawal amount
if withdrawal <= balance and withdrawal > 0:
    balance = balance - withdrawal
    print(f"Withdrawal successful! Remaining balance: R{balance:.2f}")

elif withdrawal <= 0:
    print("Invalid amount. You must withdraw more than R0.")

else:
    print("Declined. Insufficient funds")