import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_number = random.randint(0,(len(friends))) ## elements =  5 -1 : 4 > the last element is 4
print(friends[random_number],',index:',random_number)

# or

print(random.choice(friends))