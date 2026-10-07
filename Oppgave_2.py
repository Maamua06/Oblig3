import random

def num_generator():
    num = random.randrange(1,100)
    stjerne = "********"

    print(stjerne)
    print(f"***{num}***")
    print(stjerne, "\n")


for i in range(1,4):
    num_generator()
