# Write a program to add a key and value to a dictionary.   
'''
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30} 
'''

def add_new(dic, key , value):
    dic[key]=value #dic[1]=30
    return dic

dic={0: 10, 1: 20}
print(add_new(dic,2,30))