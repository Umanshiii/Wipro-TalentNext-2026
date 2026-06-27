# Write a program to insert a new item before the second element in an existing list.

def add_item(lis,item):
    lis.insert(1,item)
    
    return lis

print(add_item([1,2,35,6,7],6))