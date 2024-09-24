print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n>>  "))

if height >= 120:
    bill = 12
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n>>  "))
    if age <= 12:
        bill = 5
        print("Children tickets cost $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets cost $7.")
    else:
        print("Adult tickets cost $12.")
    wants_photo = input("Do you want a photo taken? Type Y or N \n>> ")
    if wants_photo == "Y" or wants_photo == "y" or wants_photo == "yes" or wants_photo == "YES":
        #add $3 to their bill
        bill += 3
    print(f"Your final bill is: ${bill},00.")
else:
    print("Sorry you have to grow taller before you can ride.")
