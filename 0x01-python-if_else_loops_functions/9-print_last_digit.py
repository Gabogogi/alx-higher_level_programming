#!/usr/bin/python3
def print_last_digit(number):

    if number < 0:
        modulo = abs(number) % 10
        last_digit = modulo
    else:

        last_digit = number % 10

    print("{:d}".format(last_digit), end='')
    return (last_digit)
