# Print a greeting message to the user.
print("Welcome to omazz218 restaurant tip calculator.")

# Prompt the user to enter the total bill amount.
bill = float(input("What is the total bill? $"))

# Prompt the user to enter the desired tip percentage.
tip = int(input("What percentage tip would you like to give? 12, 15, or 18? "))

# Prompt the user to enter the number of people.
people = int(input("How many people to split the bill? "))

# Calculate the tip amount.
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent

# Calculate the grand total.
total_bill = bill + total_tip_amount

# Print new line.
print("-" * 30)

# Calculate the amount each person should pay.
bill_per_person = total_bill / people
print(f"Each person should pay: ${round(bill_per_person, 2):.2f}")
print("Have a nice day!")
