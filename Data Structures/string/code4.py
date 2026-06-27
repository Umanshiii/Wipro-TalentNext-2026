# Given a string, if the first or last character is 'x', 
# return the string without those 'x' character, else return the string unchanged. 
# If the input is "xHix", then output is "Hi".

string='xUmanshix'
n=len(string)

if string[0]=='x' and string[-1]=='x':
    print(string[1:n-1])
elif string[0]=='x' and string[-1]!='x':
    print(string[1:])
elif string[0]!='x' and string[-1]=='x':
    print(string[:n-1])
else:
    print(string)
