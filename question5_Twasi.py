# Program to calculate net salary

# Accept basic salary from the user
basic_salary = float(input("Enter your basic salary: "))

# Calculate HRA (20% of basic salary)
hra = 0.20 * basic_salary

# Calculate DA (10% of basic salary)
da = 0.10 * basic_salary

# Calculate gross salary (basic + HRA + DA)
gross_salary = basic_salary + hra + da

# Calculate Tax (5% of total salary)
tax = 0.05 * gross_salary

# Calculate net salary
net_salary = gross_salary - tax

# Display the results
print("\nSalary Details:")
print(f"Basic Salary: {basic_salary:.2f}")
print(f"HRA (20%): {hra:.2f}")
print(f"DA (10%): {da:.2f}")
print(f"Tax (5% of total salary): {tax:.2f}")
print(f"Net Salary: {net_salary:.2f}")
