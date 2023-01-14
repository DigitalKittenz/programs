# bmi calculator
# height in meters, weight in kilos
# do not accept invalid values - END if its invalid with a warning!!!


# < 15 is very severely underweight
# 15.0 to 16.0 is severely underweight
# < 18.5 is underweight
# 18.5 to 24.99 is normal
# 25.0 to 29.99 overweight
# 30.0 to 34.99 is moderately obese class 1
# 35 to 40 is severely obsese class 2
# > 40 is very severely obese class 3

# calculation = kg / metres**2

print("% 45s" % "==================" + "\n% 38s" % "BMI" + "\n% 45s" % "==================")

# ok im trying a new thing and trying to catch a ValueError
# so im going to use try and except

# loops until it gets a valid input i guess.
# INPUTS:

while True:#weight
    try:
        weight = float(input("Enter your weight in KG:\t"))
        if weight <= 0:
            raise ValueError
        break
    except ValueError:
        print("Error: Invalid Weight.")
    
while True:#height
    try:
        height = float(input("Enter your height in CM:\t"))
        if height <= 0:
            raise ValueError
        break
    except ValueError:
        print("Error: Please enter a valid height")


# calculation
bmi_calc = weight / (height/100)**2

# outputs

if bmi_calc < 15:
    print("your bmi is %0.2f" % bmi_calc + " so you're very severely underweight")
elif bmi_calc > 15 and bmi_calc <= 16.0:
    print("your bmi is %0.2f" % bmi_calc + " so you're severely underweight")
elif bmi_calc < 18.5 and bmi_calc > 16.0:
    print("your bmi is %0.2f" % bmi_calc + " so you're underweight")
elif bmi_calc > 18.5 and bmi_calc < 24.99:
    print("your bmi is %0.2f" % bmi_calc + " so you're average")
elif bmi_calc > 24.99 and bmi_calc < 29.99:
    print("your bmi is %0.2f" % bmi_calc + " so you're overweight")
elif bmi_calc >= 30 and bmi_calc < 34.99:
    print("your bmi is %0.2f" % bmi_calc + " so you're obese class 1")
elif bmi_calc >= 35 and bmi_calc <= 40:
    print("your bmi is %0.2f" % bmi_calc + " so you're obese class 2")
elif bmi_calc > 40:
    print("your bmi is %0.2f" % bmi_calc + " so you're obese class 3")

