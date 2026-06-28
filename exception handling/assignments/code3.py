# Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.

def readprint():
 
    filename = input("Enter the name of the file to open: ")

    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content.title())

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found. Please check the file name and path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

print(readprint())