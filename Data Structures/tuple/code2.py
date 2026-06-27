#Write a program to check whether an element exists in a tuple or not.

tup=(2,3,5,6,78,8,9,43)
def check(tup, target):
    for i in tup:
        if i==target:
            return "The given element exists in tuple"
    
    return "The given element does not exist in tuple"

print(check(tup, 4))