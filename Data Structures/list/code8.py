# Write a program to remove the first occurrence of a specified element from a list.

def remove_first(lis, item):
    for i in range(len(lis)):
        if lis[i]==item:
            lis.remove(lis[i])
            break
    
    return lis

lis=[2,3,4,5,6,7,7,7,8,4,4,3,3]
print(remove_first(lis,7))