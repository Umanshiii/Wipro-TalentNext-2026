#Write a program to print the sum of all the digits of a given number.
'''
Example:
I/P:1234
O/P:10
'''

def sum_digits(num):
    output = 0

    while num > 0:
        digit = num % 10
        output += digit
        num //= 10

    return output
