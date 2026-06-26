#Write a program to print the sum of all the digits of a given number.
'''
Example:
I/P:1234
O/P:10
'''

def sum_digits(num):
    output=0
    for i in str(num):
        output+=int(i)
    
    return output
