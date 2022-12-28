##Name: Saraid Quinn
##Class: KCOMP_B1_Computing_with_Streams
##Lab3Ex3
#TASK: input:  centimetres
#       outputs: metres and centimetres


#input
euro = int(input("Enter an amount of money in euro:"))

twenty = euro // 20
sumOfAllTwenties = twenty * 20

ten = ((euro - sumOfAllTwenties) // 10)
sumOfAllTens = ten * 10


five = (euro - (sumOfAllTwenties + sumOfAllTens)) // 5
sumOfAllFives = five * 5

one = (euro - (sumOfAllTwenties + sumOfAllTens + sumOfAllFives)) // 1


print("In " + str(euro) + " You have:\n" + "20 Euro:   "+ str(twenty) + "\n10 Euro:   " + str(ten) + "\n5 euro:    " + str(five) + "\n1 euro:    " + str(one))
