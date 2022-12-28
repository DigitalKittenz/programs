# grade input and outputter

FULL_GRADE = 100

loop_counter = 0
student_inputted = 0

add_more = True

student_grades = ""

# adding student outside of the loop


while add_more == True:
    loop_counter += 1

    #input phrase

    student_grades = int(input("Enter grade:  "))

    student_inputted += 1

    continue_checkpoint = str(input("Add more students? y/n"))
    if continue_checkpoint == "n":
        add_more = False
        break

print("The total grades for the students are:", student_grades)
