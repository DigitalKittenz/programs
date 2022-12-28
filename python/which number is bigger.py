# Week_6_Exercise_1.i
# determine the max of 2 values using ELIF
# tell the user if both numbers are equal


print("Which Number is Bigger".center(68))

first_number = float(input("Type the first number: "))
second_number = float(input("Type the second number: "))

if first_number > second_number:
    print(f"{first_number:.2f} is bigger")

elif second_number > first_number:
    print(f"{second_number:.2f} is bigger")

elif first_number == second_number:
    print(f"{first_number:.2f} is equal to {second_number:.2f}")
