# converts inches into feet and inches

FOOT = 12 # inches
INCH = 1 / FOOT

total_inches = int(input("Enter the total number of inches: "))



total_feet = total_inches // FOOT

remaining_inches = total_inches % FOOT # the % isolates the remainder 

print(total_inches,"\" is equivalent to", total_feet, "feet", remaining_inches, "inches")


