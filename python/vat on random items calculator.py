#Ex3Lab4
#saraid quinn
#kcompb_y1
#calculate vat + total price

##########################################################
#                   WORKING OUT                          #
##########################################################
#input = price before vat -- the NET price. 
#vat = 23 or 13.5

#13.5 only is for heat, cleaning, and vet
#
###########################################################



#I WANT TO DO: IF the input is yes, print the right message.
STANDARD_VAT = 0.23
REDUCED_VAT = 0.135

print("VAT ON RANDOM ITEMS CALCULATOR".center(70))

rate = input("Is the good or service for heating, cleaning, or veterinary? Type YES or NO: ")
netPrice = float(input("Enter the net amount (before VAT) : "))
print("Net Amount: €" + "{:.2f}".format(netPrice))

if rate == 'yes' or rate == 'YES' or rate == 'Yes':
    reducedVatAmount = netPrice * REDUCED_VAT
    grossReducedVat = reducedVatAmount + netPrice
    print("Amount Vat (@13.5%): €" + "{:.2f}".format(reducedVatAmount))
    print("Total Amount (incl VAT): €" + "{:.2f}".format(grossReducedVat))
    
if rate == 'no' or rate == 'NO' or rate == 'No':
    standardVatAmount = netPrice * STANDARD_VAT
    grossStandardVat = standardVatAmount + netPrice
    print("Amount Vat (@13.5%): €" + "{:.2f}".format(standardVatAmount))
    print("Total Amount (incl VAT): €" + "{:.2f}".format(grossStandardVat))
