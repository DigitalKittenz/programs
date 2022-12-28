# SaraidQuinn.py
# Problem: split bill evenly AND ADD 15% tip

# I'm assuming that: everyone pays 15% tip

# INPUT: name of server
# INPUT: total bill amount before tip
# INPUT: number of diners

# OUTPUT: total bill amount
# OUTPUT: cost per diner

server_name = str(input("Enter your server's name: "))
total_bill_amount = float(input("Enter the total amount of the bill please: "))
diner_number = int(input("Enter the number of diners: "))

# this number is right
# I'm assuming everyones paying 15% tip here
bill_tip = ((total_bill_amount / diner_number)/100 * 15) * diner_number

# this number is right: 65.42
total_bill_with_tip = bill_tip + total_bill_amount

#this number is right
cost_each = total_bill_with_tip / diner_number

# figure this out at the end. I forgot how to do the seperation. 

print("**********HOPE YOU ENJOYED YOUR MEAL...***********", sep='* ')


print("Server\t", "  #Diners\t", "Total Bill\t", "Total (+Tip)\t", "Cost (each)\t")

print(server_name,"        ", str(diner_number),"          ", str(total_bill_amount), "           ", "%0.2f" % total_bill_with_tip, "        ","%0.2f" % cost_each)

print("**********HOPE YOU ENJOYED YOUR MEAL...***********", sep='* ')
