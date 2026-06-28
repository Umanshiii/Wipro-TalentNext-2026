#Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

import sys

def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def calculate_sum():
    if len(sys.argv) != 11:
        print(f"Usage: python {sys.argv[0]} <num1> <num2> ... <num10>")
        print("Please provide exactly 10 numbers as command-line arguments.")
        return

    prime_sum = 0
    numbers = []

    try:
        for i in range(1, len(sys.argv)):
            num = int(sys.argv[i])
            numbers.append(num)
            if prime(num):
                prime_sum += num
        print(f"The sum of prime numbers among {numbers} is: {prime_sum}")
    except ValueError:
        print("Error: All arguments must be valid integers.")

calculate_sum()

#run command: python code3.py 2 3 4 5 6 7 8 9 10 11