
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_friends=random.randint(0,4)
'''if random_friends==0:
    print("Alice")
elif random_friends==1:
    print("Bob")
elif random_friends==2:
    print("Charlie")
elif random_friends==3:
    print("David")
else:
   print("Emanuel")'''

#print(friends[random_friends])
print(random.choice(friends))
