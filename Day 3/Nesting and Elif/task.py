print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n>> "))
age = int(input("What is your age? \n>> "))
can_ride = "You can ride the rollercoaster."
if height >= 120 and height <= 230:
    if age >=18:
        print(can_ride)
        print("But you gotta pay $12.00.")
    elif age < 18 and age >=12:
        print(can_ride)
        print("But you gotta pay $7.00.")
    elif age <= 5:
        print("You are way too young mister!")
    else:
        print(can_ride)
        print("But you gotta pay $5.00.")
elif height > 230:
    print("Are you kidding me? You are telling me that you are taller that 230 cm?")
else:
    print("Sorry you have to grow taller before you can ride.")
