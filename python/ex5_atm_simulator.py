# ATM machine simulator
# use a while loop and match-case
# choice in uppercase letters
# CHOICES: DEPOSIT, WITHDRAW, EXIT
# exit says goodbye
# INFINITE deposits or withdrawals

# display to 2 decimals
# starts off with 1000 in their account


# could fix later so that its an infinity of the deposit and withdraw


print("\n"," "*15,"*"*15,"ATM SIMULATOR", "*"*15,"\n")

initial_bal = 1000
transaction_type = ""

while True:

    transaction_type = input("Please choose from the following transaction types:\n\nType D to DEPOSIT\nType W to WITHDRAW\nType X to EXIT\n\nENTER YOUR CHOICE: ").upper()

    if transaction_type == "D":
        deposit_amt = input("\nPlease enter the amount you wish to deposit: \n")
        try:
            deposit_amt = float(deposit_amt)
            initial_bal += deposit_amt
            print("Your balance is now %0.2f €" % initial_bal)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    elif transaction_type == "W":
        withdraw_amt = input("\nPlease enter the amount you wish to withdraw: \n")
        try:
            withdraw_amt = float(withdraw_amt)
            if withdraw_amt > initial_bal:
                print("Insufficient funds.")
            else:
                initial_bal -= withdraw_amt
                print("Your balance is now %0.2f €" % initial_bal)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif transaction_type == "X":
        print("\n%58s" % "Thank you for using the ATM SIMULATOR!\n")
        break
    else:
        print("Invalid choice. Try again")

