def input_student_grades():
    student_grades = []

    while True:
        grade = input("Enter grade: ")
        try:
            grade = int(grade)
            student_grades.append(grade)
        except ValueError:
            print("Invalid grade. Please enter a valid number.")

        add_more = input("Add more students? y/n")
        if add_more.lower() == "n":
            break

    return student_grades

student_grades = input_student_grades()
print("The total grades for the students are:", *student_grades)
