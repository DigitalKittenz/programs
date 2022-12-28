print("extract middle character from string")
print("but if theres an even amount of numbers, it extracts the 2 middles\n")


################################

string_input = str(input("Enter a string"))

string_input_length = len(string_input)

if string_input_length % 2 == 0:
    
    # getting index numbers and converting to ints
    # index numbers start at 0 so - 1 
    
    index_number_one = int(len(string_input)/2 - 1)
    index_number_two = int(index_number_one + 1)
    
    
    print(string_input[index_number_one],string_input[index_number_two])
    

elif string_input_length % 2 != 0:
    index_number = int(len(string_input)/2)

    print(string_input[index_number])





