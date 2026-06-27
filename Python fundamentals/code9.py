#Write a program to reverse a given number and print.
'''
Example:1
I/P: 1234
O/P:4321

Example:2
I/P:1004
O/P:4001
'''
num=int(input("Enter a number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print(reverse)