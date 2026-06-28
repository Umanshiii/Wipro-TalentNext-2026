# Write a function to return the sum of all numbers in a list.  
'''
Sample List : [8, 2, 3, 0, 7]
Expected Output : 20
'''

def total(lis):
    count=0
    for i in lis:
        count+=i
    return count

lis=[8, 2, 3, 0, 7]
print(total(lis))