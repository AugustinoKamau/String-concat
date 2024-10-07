import random

#generating even numbers randomly.
numbers = [range(0,100,2)]
#loops throgh 1-100.
for i in numbers:
    print(random.choice(i))
