#Given two non-negative values, print true if they have the same last digit such as with 27 and 57 
'''
lastDigit(7, 17) → true 
lastDigit(6, 17) → false
lastDigit(3, 113) → true
'''
input1=input("Enter the 1st number: ")   
input2=input("Enter the 2nd number: ")

if input1[-1]==input2[-1]:
    print(True)
else:
    print(False)

