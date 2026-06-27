# Project: 2
'''
Let's assume you are planning to use your Python skills to build a PBLApp for Mobile.
You decide to host your application on servers running in the cloud. You pick a hosting provider
that charges $0.51 per hour. You will launch your service using one server and want to know
how much it will cost to operate per day,per week,per month.

Write a Python program that displays the answers to the following questions:

How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How many days can I operate one server with $918?
'''

cost = 0.51 

day = cost * 24 
week = day * 7 
month = day * 30 
days = 918 / day 

print("Cost to operate one server per day: $", round(day, 2))
print("Cost to operate one server per week: $", round(week, 2))
print("Cost to operate one server per month: $", round(month, 2))
print("Number of days one server can operate with $918:", round(days, 2))