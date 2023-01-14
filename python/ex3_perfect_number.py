# perfect number
# its an int equal to the sum of its int divisors
# use a while loop to take inputs

'''find divisors by dividing it by all the numbers up to itself
and only storing values with no 0'''

start = input("Press ENTER to START the program. Press any key to exit: ")

if start == "":
    while True: # needed for the break down the bottom
        num = ""
        while not num.isnumeric() or int(num) <= 0:
            num = input("Please enter a positive integer: ")
            if not num.isnumeric() or int(num) <= 0: 
                print("Invalid input. Please enter a positive integer.")
        divisors = []
        divisor_count = 1
        while divisor_count <= int(num):
            if int(num) % divisor_count == 0:
                divisors.append(divisor_count)
            divisor_count += 1
        if sum(divisors) == int(num) * 2:
            print("This is a perfect number")
        else:
            print("This is an imperfect number")
        repeat = input("Enter another number? Press ENTER to CONTINUE, any other key to exit.")
        if repeat != "":
            break # asigned to the while true up the top
else:
    print("You've exited the program.")
