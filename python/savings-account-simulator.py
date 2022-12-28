# ======SAVINGS ACCOUNT WITHDRAWAL=====
# INPUT request the current balance
# INPUT request the amount of withdrawal
# DISPLAY new balance

# IF withdrawal > original balance = "Withdrawal denied"
# IF new balance < 150, print "Balance below €150!"


print("========Savings Account========".center(70))

import random
current_balance = random.uniform(1,77666.10)



withdrawal_permission = str(input("Do you want to withdraw: "))

if withdrawal_permission == "yes":
        print("Hello Savings User".center(70))
        display_balance = input("Display your current balance? ")
        if display_balance == "yes":
            print("€%0.2f" % current_balance)
            withdrawal_amount = float(input("Type the withdrawal amount: €"))

        new_balance = current_balance - withdrawal_amount
            
        if withdrawal_amount > current_balance:
                print("Withdrawal denied".center(70))
        elif new_balance <= 150:
            print("Balance below €150!\nWithdrawal approved\nYour current balance is: ","€%0.2f" % new_balance)
        else:
                print("Withdrawal approved\nYour current balance is: ","€%0.2f" % new_balance)


        
elif withdrawal_permission == "no":
        print("Goodbye")

else:
    print("yes or no inputs only.")



