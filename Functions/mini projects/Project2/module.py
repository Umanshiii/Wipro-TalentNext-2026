# Create a Python module
'''
ispalindrome(name): Given the user name as input, this function should
tell us whether the name is a palindrome or not.

count_the_vowels(name): Given the user name as input, this function should
tell us how many vowels are present in it.

frequency_of_letters(name): Given the user name as input, this function should
tell us how many times each letter appears in the name.

Note: name will be completely in either lower case or upper case.
Import the module in another python script and test the functions by passing
appropriate inputs.
'''
#Example
'''
Sample input 1: bob
Sample output 1:
Yes it is a palindrome.
No of vowels: 1
Frequency of letters: b-2, o-1
'''

def ispalindrome(name):
    left = 0
    right = len(name) - 1
    
    while left < right:
        if name[left] != name[right]:
            return "No it is not a palindrome"
        left += 1
        right -= 1
        
    return "Yes it is a palindrome"

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in name:
        if char in vowels:
            count += 1
            
    return f"No of vowels: {count}"


def frequency_of_letters(name):
    counts = {}
    for char in name:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
            
    output = ""
    first = True
    
    for letter in counts:
        if not first:
            output += ", "
        
        output += f"{letter}-{counts[letter]}"
        is_first = False
        
    return f"Frequency of letters: {output}"