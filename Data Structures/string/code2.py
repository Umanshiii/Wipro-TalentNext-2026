# Write a program that will check whether a given String is Palindrome or not.

s='You Do Do You'
s = s.lower()
left=0
right=len(s)-1

while left<right:

    if s[left] != s[right]:
        print("The given string is not a palindrome")
        break
    left+=1
    right-=1
  
else:
    print("The given string is palindrome")

