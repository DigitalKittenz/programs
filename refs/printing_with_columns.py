#KCOMPB-Y1
#SARAID QUINN
#Modify the following to 1. prompt the user to enter values and:
#2. print out the formatted version.


moduleName = "Programming"
numberOfStudents = 45
averageMark = 79.6

print("%-15s %-15s %15s " %("Module Name", "Number of Students", "AverageMark"))

print("%-15s %-22d %0.2f" %(moduleName, numberOfStudents, averageMark))



moduleName = input("Enter the module name ")
numberOfStudents = int(input("How many students take " + moduleName + "? "))
averageMark = float(input("What is the average mark in " + moduleName + "? "))



print("%-15s %15s %15s " %("Module Name", "Number of Students", "AverageMark"))
print("%-15s %-22d %-0.2f " %(moduleName, numberOfStudents, averageMark))


