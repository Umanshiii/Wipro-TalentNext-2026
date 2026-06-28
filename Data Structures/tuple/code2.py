#Write a program to check whether an element exists in a tuple or not.

tup=(2,3,5,6,78,8,9,43)
target=int(input('Enter target: '))
for i in tup:
    if i==target:
        print("The given element exists in tuple")
        break
else:
    print("The given element does not exist in tuple")
