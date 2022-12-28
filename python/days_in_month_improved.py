
# Program to output the number of days in the month given the month as a number:

month = int(input("Please enter the month number:"))

# 4 months have 30 days.

days_print_output = "Number of days in this month is: "

if month == 4 or month == 6 or month == 9 or month == 11:
    print(days_print_output + "30 days")
elif month == 2:
    print(days_print_output + "28 days; 29 if leap year.")
else:
    print(days_print_output + "31")

