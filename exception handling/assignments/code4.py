# Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.

def check():

    lis = [10, 20, -15, 30, -25, 40, -35, 50, -45, 2]

    print(f"The list is: {lis}")

    try:
        index = int(input("Enter an index: "))
        num = lis[index]

        if num >= 0:
            print(f"The number at index {index} is {num}, which is a positive number (or zero).")
        else:
            print(f"The number at index {index} is {num}, which is a negative number.")

    except ValueError:
        print("Error: Invalid input. Please enter an integer for the index.")
    except IndexError:
        print(f"Error: Index {index} is out of bounds. Please enter an index between 0 and {len(lis) - 1}.")

print(check())