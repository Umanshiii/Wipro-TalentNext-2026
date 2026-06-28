# Write a program to accept two numbers from the user and perform division. 
# If any exception occurs, print an error message or else print the result.

def division():
    try:
        num1 = float(input("Enter the first number (numerator): "))
        num2 = float(input("Enter the second number (denominator): "))
        
        result = num1 / num2
        return f"The result of the division is: {result}"
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
        
    except ValueError:
        return "Error: Invalid input. Please enter valid numbers."
        
    except Exception as e:
        return f"An unexpected error occurred: {e}"

print(division())