print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10%, 12%, 15%?\n"))
people = int(input("How many people to split the bill?\n"))

# 12 % = 12 / 100 = 0.12
percentage_tip = tip / 100
print(f" percentage tip: {percentage_tip}")
# round to 2 digits
total_bill = round((bill + (bill * percentage_tip)) / people,2)

print(f"bill: ${bill}")
print(f"tip: {tip}%")
print(f"people count: {people}")
#add always 2 digits after ".": .2f
print(f"Total bill: ${total_bill:.2f}.")
