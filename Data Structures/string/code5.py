# Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. 
# You may assume that n is between 0 and the length of the string inclusive. 
# For example if the inputs are “Wipro” and 3, then the output should be “propropro”.

string='umanshi'
result=''
for i in range(len(string)-n,n+2):
    result+=string[i]
print(result*n)
