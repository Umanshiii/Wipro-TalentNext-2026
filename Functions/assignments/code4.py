# Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.

def count(s):    
    upper=0
    lower=0

    for i in s:
        if 65<=ord(i)<=90:
            upper+=1
        elif 97<=ord(i)<=122:
            lower+=1

    return f"Upper case character count = {upper} and Lower case character count = {lower}"

s='MyNameISUmanshi'
print(count(s))



