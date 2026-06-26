#Write a program to reverse a given number and print.
'''
Example:1
I/P: 1234
O/P:4321

Example:2
I/P:1004
O/P:4001
'''

def rev(num):
    reverse=''
    for i in range(len(str(num))-1,-1,-1):
        reverse+=str(num)[i]
    return int(reverse)