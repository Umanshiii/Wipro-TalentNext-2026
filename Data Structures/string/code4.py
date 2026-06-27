# Given a string, if the first or last character is 'x', 
# return the string without those 'x' character, else return the string unchanged. 
# If the input is "xHix", then output is "Hi".

def change(string):
    n=len(string)
    if string[0]=='x' and string[-1]=='x':
        return string[1:n-1]
    elif string[0]=='x' and string[-1]!='x':
        return string[1:]
    elif string[0]!='x' and string[-1]=='x':
        return string[:n-1]
    else:
        return string

string='xUmanshix'
print(change(string))