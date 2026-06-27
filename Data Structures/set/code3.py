# Write a program to create an union of sets.

def union(set1, set2):
    if len(set1)<len(set2):
        small=set1
        large=set2
    else:
        small=set2
        large=set1
    result=set()
    for i in large:
        if i in result:
            continue
        result.add(i)
        
    for i in small:
        if i in result:
            continue
        result.add(i)

    return result

set1={2,3,4,6,67,8}
set2={3,4,6,77,24,5}
print(union(set1,set2))