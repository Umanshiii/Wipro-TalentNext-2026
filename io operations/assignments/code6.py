# Write a program to count the frequency of a user entered word in a txt file.

import re

def count(filepath, words):

    frequency = 0
    with open(filepath, 'r') as file:
        target_word_lower = word_to_find.lower()
        for line in file:
            words_in_line = re.findall(r'\b\w+\b', line.lower())
            frequency += words_in_line.count(target_word_lower)
    return frequency

path = input("Enter the path to the text file: ")
search = input("Enter the word to count: ")

word = count(path, search)

print(f"The word '{search}' appears {word} time(s) in the file.")