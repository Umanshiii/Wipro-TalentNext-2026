# Write a program to read first n lines from a txt file. Get n as user input

def read_lines(filepath, n):
    with open(filepath, 'r') as file:
        for i, line in enumerate(file):
            if i < n:
                print(line.strip())
            else:
                break

path = input("Enter the path to the text file: ")
lines = int(input("Enter the number of lines to read: "))
if lines < 0:
    print("Please enter a non-negative number of lines.")
else:
    read_lines(path, lines)
