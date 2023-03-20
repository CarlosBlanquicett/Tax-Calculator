# Call the function to start the game
play_game()

# Prompt the user for gross income and number of dependents
gross_income = float(input("Enter your gross income: "))
num_dependents = int(input("Enter the number of dependents: "))

# Calculate the taxable income by subtracting the standard deduction and dependent deductions
taxable_income = gross_income - 10000 - (num_dependents * 3000)

# Calculate the income tax as 20% of the taxable income
income_tax = 0.2 * taxable_income

# Print the income tax as a decimal number
print("Your income tax is: $", "{:.2f}".format(income_tax))