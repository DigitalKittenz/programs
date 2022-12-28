# Prompt the user to find out which calculation is required:
# Area of a circle, volume of a sphere, or volume of a cylinder.
# CALCULATE then OUTPUT the chosen result.

# area of a circle = pi x (radius ** 2)
# volume of a sphere = (4/3) * (pi * radius ** 3)
# volume of a cylinder = pi * (radius ** 2) * height

PI_CONSTANT = 3.14

print("~~I CALCULATE:~~".center(68)+"\n1. Area of a circle\t2. Volume of a sphere\t3. Volume of a cylinder\n"+"~"*71)
calculation_choice = input("What calculation do you want me to do?\nTYPE 1, 2, or 3:  ")


if calculation_choice == "1":
    circle_radius = float(input("Type the radius of your circle: "))
    circle_volume = PI_CONSTANT * (circle_radius ** 2)
    print("Area of the circle:", "%0.2f" % circle_volume, "cm2")

elif calculation_choice == "2":
    sphere_radius = float(input("Type the radius of your sphere:  "))
    sphere_volume = (4 / 3) * (PI_CONSTANT * sphere_radius ** 3)
    print("Volume of the sphere:" , "%0.2f" % sphere_volume, "m2")

elif calculation_choice == "3":
    cylinder_radius = float(input("Type the radius of your cylinder: "))
    cylinder_height = float(input("Type the height of your cylinder: "))
    cylinder_volume = PI_CONSTANT * (cylinder_radius ** 2) * cylinder_height
    print("Volume of the cylinder:", "%0.2f" % cylinder_volume, "m2")

else:
    print("Try again and choose a calculation")

    
                          
