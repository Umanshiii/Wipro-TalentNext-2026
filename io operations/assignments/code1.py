# Write a program to read the entire content from a txt file and display it to the user.

def displayfile(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
        print(content)

path = input("Enter the path to the text file you want to read: ")
print(displayfile(path))
