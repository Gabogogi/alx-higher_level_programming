#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    modulo = abs(number) % 10
    l_digit = modulo * -1
else:
    modulo = number % 10
    l_digit = modulo

if l_digit == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif l_digit > 5:
    print(f"Last digit of {number} is {l_digit} and is greater than 5")
else:
    print(f"Last digit of {number} is {l_digit} and is less than 6 and not 0")
