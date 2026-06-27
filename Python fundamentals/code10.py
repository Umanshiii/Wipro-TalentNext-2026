#Write a program to find if the given number is palindrome or not
'''
Example:1
I/P:110011
O/P: 110011 is a palindrome.

Example:2
I/P:1234
O/P: 1234 is not a palindrome.
'''

num=int(input("Enter a number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num == reverse:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")