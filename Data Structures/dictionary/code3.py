#Write a program to check if a given key already exists in a dictionary.

def check(dic1, target):

    for key in dic1.keys():
        if key==target:
            return "Given key already exists in the dictionary"

    return "The Given key does not exists in the dictionary"

dic1={1:10, 2:20}  
print(check(dic1, 3))