import random

members = ["Bill", "John", "Joe", "Chris"]
leader = random.choice(members)
print(leader)
for i in range(3):
    rand = random.randint(10,30)
    print(rand)