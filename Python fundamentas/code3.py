#Given two non-negative values, print true if they have the same last digit such as with 27 and 57 
'''
lastDigit(7, 17) → true 
lastDigit(6, 17) → false
lastDigit(3, 113) → true
'''

def lastdigit(num1, num2):
    input1=str(num1)
    input2=str(num2)

    if input1[-1]==input2[-1]:
        return True
    else:
        return False

lastdigit(56,78)