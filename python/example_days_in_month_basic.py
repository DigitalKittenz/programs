
# Program to output the number of days in the month given the month as a number:

month = int(input("Please enter the month number:"))

if(month == 1):
    days_in_month = 31
elif(month == 2):
    days_in_month = 28
elif(month == 3):
    days_in_month = 31
elif(month == 4):
    days_in_month = 30
elif(month == 5):
    days_in_month = 31
elif(month == 6):
    days_in_month = 30
elif(month == 7):
    days_in_month = 31
elif(month == 8):
    days_in_month = 31
elif(month == 9):
    days_in_month = 30
elif(month == 10):
    days_in_month = 31
elif(month == 11):
    days_in_month = 30
else:
    days_in_month = 31


print("Number of days in this month is %d" %(days_in_month))
