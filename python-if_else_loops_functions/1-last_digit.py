#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = int(str(number)[-1:])
if number < 0:
    last_number = -last_number
print(f"Last digit of {number} is {last_number} and is ", end='')
if last_number == 0:
    print(0)
elif last_number > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
