# Write a program to find the maximum and minimum value in a set.

def min_and_max(data):
    minimum=float('inf')
    maximum=0

    for i in data:
        if i<minimum:
            minimum=i
        if i>maximum:
            maximum=i
    
    return f"Minimum = {minimum} and Maximum = {maximum}"

data={2,3,5,6,8,9}
print(min_and_max(data))