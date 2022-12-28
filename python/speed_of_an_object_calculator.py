
##Name: Saraid Quinn
##Class: KCOMP_B1_Computing_with_Streams
##Lab2Ex6_2
#TASK: calculate output speed when given a value for distance and time.

print("SPEED OF AN OBJECT CALCULATOR".center(70))

def speed(distance,time):
    print("speed = ")
    return (distance/time)

distance = int(input("Enter the distance: "))
time = int(input("Enter the time: "))

speed = distance/time

print (("Distance: "),(distance),(" Time: "),(time),("hr"))
print (("Speed is: "),(speed),("km/hr"))
