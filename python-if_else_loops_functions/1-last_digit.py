#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
delim = -10 if number < 0 else 10
print("Last digit of {} is {} and is".format(number, number % delim), end=" ")
if number % delim > 5:
    print("greater than 5")
elif number % delim == 0:
    print("0")
else:
    print("less than 6 and not 0")
