#  Write a program to accept input from user and append it to a txt file.

def appendfile(filepath, text):

    with open(filepath, 'a') as file:
        file.write(text_to_append + '\n')

path = input("Enter the path to the text file: ")
text = input("Enter the text you want to append to the file: ")
print(appendfile(path, text))