
print("Welcome to Python Pizza Deliveries!")
price = 0
size = input("What size pizza do you want? S, M or L:\n ")
if size == 'S':# Small pizza (S): $15
    price = int(15)
if size == 'M':# Medium pizza (M): $20
    price = int(20)
if size == 'L':# Large pizza (L): $25
    price = int(25)


pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
if pepperoni == 'Y':
    if size == 'S':
        price += 2 # Add pepperoni for small pizza (Y or N): +$2
    else:
        price += 3 # Add pepperoni for medium or large pizza (Y or N): +$3


# Add extra cheese for any size pizza (Y or N): +$1
extra_cheese = input("Do you want extra cheese? Y or N: \n")
if extra_cheese == 'Y':
    price += 1

print(f"Your final bill is: ${price}.")
