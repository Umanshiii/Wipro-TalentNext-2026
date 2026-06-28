# Write a function to print the even numbers from a given list. 
# List is passed to the function as an argument. 
'''
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
'''

def show(lis):
    result= []
    for i in lis:
        if i%2==0:
            result.append(i)
            
    return result

print(show([2,5,4,67,1,86,79,990,90]))