# Write a program to print prime numbers between 10 and 99.

for i in range(10,100):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)