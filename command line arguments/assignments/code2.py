# Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.
import sys

def display():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} \"<Your Welcome Message>\"")
        print("Please provide a welcome message as a command-line argument.")
        return

    file_name = sys.argv[0]
    welcome_message = sys.argv[1]
    print(f"File Name: {file_name}")
    print(f"Welcome Message: {welcome_message}")

display()

#run the command: python code4.py "Welcome to the Wipro TalentNext 2026 Program!"