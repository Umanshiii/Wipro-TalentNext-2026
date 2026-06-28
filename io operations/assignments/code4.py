# Write a program to read contents from a txt file line by line and store each line into a list.

def read_file(filepath):
    lines = []
    with open(filepath, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines

path = input("Enter the path to the text file: ")
contents = read_file(path)

print("Contents of the file (line by line in a list):")
print(contents)