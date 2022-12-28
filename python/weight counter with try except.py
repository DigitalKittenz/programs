# lab 8 ex 4

# read in weights of 5 people
# display 2 decimals: av weight, % whos 80kg AT LEAST.

welcome_phrase = "Enter the weights for the 5 people"

print(f'{welcome_phrase:*^70}')

weight_counter = 1

weight_list = []

weight_prompt = f"Enter the weight of person"

at_least_eighty = []

while weight_counter < 6:
    print(weight_prompt, weight_counter)
    try:
        weight_input = int(input(": "))
    except ValueError:
        print("Invalid input. Please enter a valid weight.")
        continue
    if weight_input >= 80:
        at_least_eighty += [weight_input]
    weight_list += [weight_input]
    weight_counter += 1
    
average_weight = sum(weight_list) / len(weight_list)

print("The average weight is: ", average_weight, "\nover 80s are:", ', '.join(map(str, at_least_eighty)))

# all i have to do is format
