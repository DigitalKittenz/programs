##Name: Saraid Quinn
##Class: KCOMP_B1_Computing_with_Streams
##Lab3Ex3
#TASK: input:  centimetres
#       outputs: metres and centimetres


#input
cm = int(input("Enter centimetres..."))

metres = cm // 100
decimalCM = cm % 100

print(str(cm) + "cm is equal to: " + str(metres) + " metres and " + str(decimalCM) + "cm.")
