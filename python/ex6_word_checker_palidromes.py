# inputs exactly 9 characters
# if its not exactly 9, quit the program
# if its 9 - check if a palidrome

print("% 20s" % " " + "9 Letter Palidrome Checker")

'''while loop for input -
i want it to continue if the wrong input is there
so they can try again'''

while True:
    word = str(input("Please enter a word 9 characters long:"))
    if len(word) == 9:
        print("9")
        break
    else:
        print("Invalid length - try again.")
        continue

if word == word[::-1]:
    print("The word", word, "is a palidrome")
else:
    print("The word", word, "is not a palidrome")
    
