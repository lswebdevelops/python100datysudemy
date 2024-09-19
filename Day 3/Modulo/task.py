print("############\nChecking odd or even.\n############")

input_number = input("Type a number\n>>  ")

check_number = int(input_number) % 2

if check_number == 0:
    print(f"Your typed number ({input_number}) is even.")
else:
    print(f"Your typed number ({input_number}) is odd.")
