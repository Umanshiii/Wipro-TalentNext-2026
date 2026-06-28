# Write a program to accept a number from the user and check whether it’s prime or not. If user enters anything other than number, handle the exception and print an error message.

def check_prime():
    try:
        num = int(input("Enter a number to check if it's prime: "))
        
        if num <= 1:
            print(f"{num} is not a prime number.")
            return

        for i in range(2, num):
            if num % i == 0:
                return f"{num} is not a prime number."
        else:
            return f"{num} is a prime number!"

    except ValueError:
        return "Error: Invalid input. Please enter a valid whole number."
        
print(check_prime())