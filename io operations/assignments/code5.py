# Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.

import re

def find_longest(filepath):

    longest_word = "" 

    with open(filepath, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                if len(word) > len(longest_word):
                    longest_word = word
                    
    return longest_word

path = input("Enter the path to the text file: ")
longest = find_longest(path)
if longest:
    print(f"The longest word in the file is: {longest}")
else:
    print("No words found or an error occurred.")