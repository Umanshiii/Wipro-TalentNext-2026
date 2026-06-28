# Write a function to calculate and return the factorial of a number (a non-negative integer).

def fact(x):
    if x==0:
        return 1
    
    return x*fact(x-1)

print(fact(5))