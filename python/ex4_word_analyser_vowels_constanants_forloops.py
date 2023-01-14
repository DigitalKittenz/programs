# display with 2 decimal places
# use 2 for loops


# reads in 5 words


# determine the average # of vowels per word
# determine average number of consonants
# validation check - they are LETTERS and 5 words

# store the longest word


word = ""
word_list = []
longest_word = ""
vowels = 0
consonants = 0
count = 0

for i in range(5):
    word = input(f"Please enter word {count + 1}: ")
    if word.isalpha():
        count += 1
        word_list.append(word)
        for letter in word:
            if letter in "aeiouAEIOU":
                vowels += 1
            else:
                consonants += 1
                
        if len(word) > len(longest_word):
            longest_word = word
    else:
        print("Invalid. Please try again.")

# output
print("The average number of vowels per word: %0.2f" % (round(vowels/count, 2)))
print("The average number of consonants per word: %0.2f" % (round(consonants/count, 2)))
print("The longest word:", longest_word)

