#Write a program to check if a given number is prime or not

def prime(num):
    if num<=1:
        return "Not Prime"
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        return "Prime"
    else:
        return "Not prime"