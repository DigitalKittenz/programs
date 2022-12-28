# ex 2
# read grade of 8 students
# then calculates and outputs the average

welcome = ("Enter the grades of 8 students")
print(f'{welcome:*^60}')
grade_list = []

lower_forty = []

higher_eighty = []

grade_counter = 1

while grade_counter < 9:
    print("Enter grade",grade_counter)
    grade = (int(input(": ")))
    #adding lower 40 and higher 80 to seperate lits
    if grade == 40 or grade < 40:
        lower_forty += [grade]
    elif grade == 80 or grade > 80:
        higher_eighty += [grade]
    #trying to add to the list
    grade_list += [grade]
    #print(grade_counter)
    grade_counter += 1

print("The grade list is:\t", *grade_list)
print(*lower_forty)

# average

average = sum(grade_list)/len(grade_list)

count_lower = len(lower_forty)
count_higher = len(higher_eighty)


print("The class average is:", int(average),"%")

print(f"The number of students who received {40} or lower:", count_lower,
      f"\nThe number of students who received {80} or higher:", count_higher)
