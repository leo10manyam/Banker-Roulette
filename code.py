import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# first option
print(random.choice(friends))
# second option 
random_index = random.randint(0,4)
print(friends[random_index])
