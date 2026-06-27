#Write a program to check if a given number is prime or not

num=int(input())
if num<=1:
    print("Not Prime")
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("Not prime")