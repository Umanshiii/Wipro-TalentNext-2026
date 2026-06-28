# Write a function to return the reverse of a string.  
'''
Sample String : "1234abcd"
Expected Output : "dcba4321"
'''

def rev(string):
    result=''

    for i in range(len(string)-1,-1,-1):
        result+=string[i]
    
    return result

string='umanshi'
print(rev(string))