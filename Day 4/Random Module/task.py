import random
# import my_module
# rand_number = random.randint(1, 10)
#
# print(rand_number)
# print(my_module.phase)
#
#
#
# print(random.random() * 10) # 0 to 9.999999
#
# print(random.uniform(1,5)) # 2.425058174726192
#
#

heads_or_tails = random.randint(0,1)
heads_or_tails_letter = ""
user_choice = input("Type H for Heads or T for Tails:\n> ")


if heads_or_tails == 1:
    heads_or_tails_letter = "T"
elif heads_or_tails == 0:
    heads_or_tails_letter = "H"


if user_choice != "T" and user_choice != "H":
    print("Wrong choice!")
elif user_choice == heads_or_tails_letter:
    print("You got it!")
    if user_choice == "T":
        print("It's Tails")
    elif user_choice == "H":
        print("It's Heads.")
else:
    print("Not lucky today.")




