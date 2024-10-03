import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = input("Type R for rock,\n S for Scissors\n or P for paper.\n> ")
if user_choice != "R" and user_choice != "S" and user_choice != "P":
    print("Try again. Type 'R', 'S' or 'P'.")
else:
    random_number = random.randint(0,2)
    pc_choice = ''
    if random_number == 0:
        pc_choice = "R"
    elif random_number == 1:
        pc_choice = "S"
    elif random_number == 2:
        pc_choice = "P"
    # rock
    # if user_choice == "R" and pc_choice == "R":
    #     print("A tie")
    # if user_choice == "R" and pc_choice == "P":
    #     print("You win")
    # if user_choice == "R" and pc_choice == "S":
    #     print("You lose")
    # # paper
    # if user_choice == "P" and pc_choice == "P":
    #     print("A tie")
    # if user_choice == "P" and pc_choice == "R":
    #     print("You win")
    # if user_choice == "P" and pc_choice == "S":
    #     print("You Lose")
    # #scissors
    # if user_choice == "S" and pc_choice == "S":
    #     print("A tie")
    # if user_choice == "S" and pc_choice == "P":
    #     print("You win")
    # if user_choice == "S" and pc_choice == "R":
    #     print("You Lose")
## better code;
    if user_choice == "R":
        if pc_choice == "R":
            print("A tie")
        elif pc_choice == "P":
            print("You lose")
        else:  # pc_choice == "S"
            print("You win")
    elif user_choice == "P":
        if pc_choice == "P":
            print("A tie")
        elif pc_choice == "R":
            print("You win")
        else:  # pc_choice == "S"
            print("You lose")
    elif user_choice == "S":
        if pc_choice == "S":
            print("A tie")
        elif pc_choice == "P":
            print("You win")
        else:  # pc_choice == "R"
            print("You lose")

    #printing user's choice
    if user_choice == "R":
        print("User chose:")
        print(rock)
    if user_choice == "S":
        print("User chose:")
        print(scissors)
    if user_choice == "P":
        print("User chose:")
        print(paper)
    #printing random choice
    if pc_choice == "R":
        print("Pc chose:")
        print(rock)
    if pc_choice == "S":
        print("Pc chose:")
        print(scissors)
    if pc_choice == "P":
        print("Pc chose:")
        print(paper)
