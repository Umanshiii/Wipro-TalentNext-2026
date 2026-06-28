# Write a program to find the maximum and minimum value in a set.


data={2,3,5,6,8,9}
minimum=float('inf')
maximum=0

for i in data:
    if i<minimum:
        minimum=i
    if i>maximum:
        maximum=i
    
print(f"Minimum = {minimum} and Maximum = {maximum}")

print(min_and_max(data))