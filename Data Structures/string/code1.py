# Write a program to count the number of upper and lower case letters in a String.

s='ThisIsTheString'
def count_letters(s):
    upper=0
    lower=0

    for i in s:
        if 65<=ord(i)<=90:
            upper+=1
        elif 97<=ord(i)<=122:
            lower+=1

    return f"Upper case character count = {upper} and Lower case character count = {lower}"

print(count_letters(s))