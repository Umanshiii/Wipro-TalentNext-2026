# Write a program that will check whether a given String is Palindrome or not.

def palindrome(s):
    s = s.lower()
    left=0
    right=len(s)-1

    while left<right:

        if s[left] != s[right]:
            return "The given string is not a palindrome"
        left+=1
        right-=1

    
    else:
        return "The given string is palindrome"

s='You Do Do You'
print(palindrome(s))