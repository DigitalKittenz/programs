#Ex4Lab4 -- distance travelled by an object
#distance travelled by an object =
#####     distance = (initial_speed)(time spent travelling) +
#                                       (1/2) * acceleration * (time)**2
#
#AIM: make a program that reads for: initial speed, time, and acceleration
######    and determines the distance travelled by the object. (float).

print("Distance travellled by an object calculator".center(70))
print("All inputs are in seconds".center(70))

initial_speed = float(input("Enter initial velocity (U): "))


acceleration = float(input("Enter acceleration - meters per seconds (A): "))


time_travelling = float(input("Enter time taken to travel (T): "))


distance = (initial_speed * time_travelling)+((1/2)*acceleration*(time_travelling)**2)

print("Object travelled ", "%.2f" % distance + str(" meters"))




