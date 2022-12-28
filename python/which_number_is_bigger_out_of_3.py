# Week_6_Exercise_1.ii
# determine the max of 2 values using ELIF
# tell the user if both numbers are equal


print("Check which number is bigger out of 3".center(68))

first_number = float(input("Type the first number: "))
second_number = float(input("Type the second number: "))
third_number = float(input("Type the third number: "))

if first_number > second_number and first_number > third_number:
    print(f"{first_number:.2f} is bigger")

elif second_number > first_number and second_number > third_number:
    print(f"{second_number:.2f} is bigger")

elif third_number > first_number and third_number > second_number:
    print(f"{third_number:.2f} is bigger")

else:
    print("All values are the same!")
