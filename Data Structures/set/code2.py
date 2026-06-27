# Write a program to create an intersection of sets.

def intersection(set1, set2):
    if len(set1)<len(set2):
        small=set1
        large=set2
    else:
        small=set2
        large=set1
    result=set()
    for i in small:
        if i in large:
            result.add(i)

    return result

set1={2,3,4,6,67}
set2={3,4,6,77,2}
print(intersection(set1,set2))
