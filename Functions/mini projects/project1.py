#Create a python function
'''
Write a Python function that accepts a hyphen-separated sequence of colors
as input and returns the colors in a hyphen-separated sequence after sorting
them alphabetically.

Constraint: All the colors will be completely in either lower case or upper case.

Sample input 1: green-red-yellow-black-white
Sample output 1: black-green-red-white-yellow

Sample input 2: PINK-BLUE-TAN-PURPLE
Sample output 2: BLUE-PINK-PURPLE-TAN
'''
def colors(string):

    lis = string.split('-')
    lis.sort()
    return '-'.join(lis)


print(colors('PINK-BLUE-TAN-PURPLE'))