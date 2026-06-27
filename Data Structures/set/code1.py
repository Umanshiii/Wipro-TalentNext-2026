#Write a program to remove a given item from the set.

def remove_item(data, item):
    
    for i in data:
        if i==item:
            data.remove(item)
            
    else:
        return "Item not found"

    return data

data=set(['My', 'Name', 'Is', 'Umanshi'])
print(remove_item(data, 'item'))