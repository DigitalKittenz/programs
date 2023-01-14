# torus tube radius calculator

#inputs


#a
tube_radius = float(input("Please enter the torus's TUBE RADIUS: "))
#b
cross_sect_radius = float(input("Please enter the torus's CROSS-SECTION RADIUS: "))
#m
mass = float(input("Please enter the torus's MASS: "))

# maths part

diam_inertia = ((1 / 8) *(4 * tube_radius ** 2) + (5 * cross_sect_radius ** 2)) * mass

vert_axis = (tube_radius ** 2) + (3 / 4 * cross_sect_radius ** 2) * mass

#

print("\n"+"="*6+"Results"+"="*6+"\n")

print("Moment of inertia about a diameter is: %0.3f sq m" % diam_inertia)
print("Moment of inertia about a vertical axis is: %0.3f sq m" % vert_axis)


