# input a float value for variable a here
# input a float value for variable b here

# output the result of addition here
# output the result of subtraction here
# output the result of multiplication here
# output the result of division here



variable_a = float(input("Variable A float: \n"))
variable_b = float(input("Variable B float: \n"))

sum_chosen = int(input("Which sum?\n1. addition + \n2. subtraction - \n3. multiplication *\n4. division /\n5. All\n"))

variable_sum = variable_a + variable_b

#addition
if sum_chosen == 1:
    variable_sum = variable_a + variable_b
#subtraction
elif sum_chosen == 2:
    variable_sum = variable_a - variable_b
#multiplication
elif sum_chosen == 3:
    variable_sum = variable_a * variable_b
#division
elif sum_chosen == 4:
    variable_sum = variable_a / variable_b
#all
elif sum_chosen == 5:
    addition = variable_a + variable_b
    subtraction = variable_a - variable_b
    multiplication = variable_a * variable_b
    division = variable_a / variable_b
    print(" + %0.2f" % addition,"\n - %0.2f" % subtraction, "\n * %0.2f" % multiplication,"\n \\ %0.2f" % division,"\n")
else:
    print(str(sum_chosen) + "is invalid")

if sum_chosen != 5:
    print(variable_sum)
