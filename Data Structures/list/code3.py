#Write a program to reverse the order of the items in the list.

def reverse(lis):
    left = 0
    right = len(lis) - 1
    
    while left < right:
        lis[left], lis[right] = lis[right], lis[left]
        left += 1
        right -= 1
        
    return lis

lis = [10, 20, 30, 40, 50]
print("Original:", lis)
print("Reversed:", reverse(lis))
