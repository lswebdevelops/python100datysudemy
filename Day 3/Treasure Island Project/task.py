
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
question_1 =  input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n  ').lower()
if question_1 == "left":
    question_2 =input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n  ').lower()
    if question_2 == "wait":
        question_3 =  input("You arrive at the island unharmed. "
                        "There is house with 3 doors. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose?\n  ").lower()
        if question_3 == "yellow":
            print("You are the Winner!!!")
        elif question_3 == "red":
            print("It's a room full of fire. Game over!")
        elif question_3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("The non-existing-color door abducted you. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell in to a hole. Game Over.")
    

    