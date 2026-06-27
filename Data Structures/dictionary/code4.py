#Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.

dic={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
print("Keys of dictionary")
for key in dic.keys():
    print(key,end=' ')
print()
print("Values of dictionary")
for val in dic.values():
    print(val,end=' ')
print()
print("Keys and Values of dictionary")
for key,val in dic.items():
    print(f"{key} = {val}")


