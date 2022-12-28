#How many stamps to post a number of letters?

print("How many stamps do you need to post a letter?".center(71))
print("You can fit 5 letters in an envelope".center(71))

stampCost = 1.25

letterAmount = int(input("How many letters? "))
stampsPerLetter = letterAmount / 5

import math
ceilingStampNumber = math.ceil(stampsPerLetter)


print("Stamps needed: " + str(ceilingStampNumber) + " stamps for " + str(letterAmount) + " letters.")
      
