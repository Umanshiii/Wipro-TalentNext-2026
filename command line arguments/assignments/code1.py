# Write a program to accept two numbers as command line arguments and display their sum.

import sys

def calculate_sum():
    if len(sys.argv) != 3:
        print("Usage: python code1.py <number1> <number2>")
        return

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(f"The sum is: {num1 + num2}")
    
calculate_sum()

#run the command: python code1.py 15 27