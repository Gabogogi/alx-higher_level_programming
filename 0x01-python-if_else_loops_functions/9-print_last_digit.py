#!/usr/bin/python3
def print_last_digit(number):

    if number < 0:
        modulo = abs(number) % 10
        last_digit = modulo * -1
    else:

        last_digit = number % 10

    return print(last_digit)
