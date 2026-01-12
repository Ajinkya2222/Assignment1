# Store user's initial balance
balance = 10000  # example balance

# Take withdrawal amount as input
withdraw = int(input("Enter withdrawal amount: "))

# Check if amount is a multiple of 100
if withdraw % 100 != 0:
    print("Withdrawal amount must be a multiple of 100.")

# Check if balance is sufficient
elif withdraw > balance:
    print("Insufficient balance.")

# If all conditions are satisfied
else:
    balance -= withdraw
    print("Withdrawal successful!")
    print("Updated Balance:", balance)