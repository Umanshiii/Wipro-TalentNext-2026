#Write a program to print the number of occurrences of a specified element in a list.

def count(lis, target):
    total=0

    for i in lis:
        if i==target:
            total+=1

    return total

print(count([1,2,3,4,5,3,2,4,2,5,2,5],2))