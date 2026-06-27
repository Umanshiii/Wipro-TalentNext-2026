# Write a program to sum all the values in a dictionary, considering the values will be of int type.

def sum_of_values(dic):
    total=0
    for i in dic.values():
        total+=i

    return total

dic={0: 10, 1: 20, 2: 30}
print(sum_of_values(dic))