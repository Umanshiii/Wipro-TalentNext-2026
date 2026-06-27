#Write a program to append the items of list1 to list2 in the front.

def add_item(list1, list2):

    for i in list1:
        list2.insert(0,i)
        
    return list2

print(add_item([2,3,4,5,6],[6,5,4,3,2]))
