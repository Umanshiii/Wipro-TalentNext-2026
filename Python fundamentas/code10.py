#Write a program to find if the given number is palindrome or not
'''
Example:1
I/P:110011
O/P: 110011 is a palindrome.

Example:2
I/P:1234
O/P: 1234 is not a palindrome.
'''

def palindrome(num):
    reverse=''
    for i in range(len(str(num))-1,-1,-1):
        reverse+=str(num)[i]
    if num==int(reverse):
        return f"{num} is a palindrome"
    else:
        return f"{num} is not a palindrome"