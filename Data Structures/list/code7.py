#Write a program to remove the item from a specified index in a list.

def delete(lis, index):
    lis.remove(index)
    return lis

lis=[2,3,4,6,78,8]
print(delete(lis,3))