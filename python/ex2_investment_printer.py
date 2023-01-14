'''
This program will:
                1. enter investment type
                2. enter number of purchased shares (int)
                3. enter current share price.
output:
        single print display using format specifiers
        to 4 decimal places.
        investment details is printed using special tab characters.
'''
# investment portfolio for share

# first

first_invest = str(input("Enter the first investment: "))
first_share_purchase = int(input("Enter the number of shares purchased: "))
first_share_price = float(input("Enter the share price: "))

# second

second_invest = str(input("Enter the TYPE of the second investment: "))
second_share_purchase = int(input("Enter the number of shares purchased: "))
second_share_price = float(input("Enter the share price: "))

# output
print("% 45s" % "==================" + "\n% 45s" % "Investment Details" + "\n% 45s" % "==================")

print("Investment Type" + "% 18s" % "# Shares" + "% 18s" % "Share Price")


print("----------------" + "% 20s" % "-------------" + "% 17s" % "-------------")

print(first_invest + "    " + "% 25s" % str(first_share_purchase) + "   " + "% 15.2f" % first_share_price)
print(second_invest + "    " + "% 25s" % str(second_share_purchase) + "   " + "% 15.2f" % second_share_price)
