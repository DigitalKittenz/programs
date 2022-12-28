# bookstore has a KB day sale every October 24 (10.24)

# IF: #A# 8% discount if the price is less than $128
# #B# 16% discount if the price is at least $128

DISCOUNT_DAY = "october 24" and "1024"

book_price = float(input("What is the cost of the book?"))

the_date = str(input("What is the date?"))

if the_date != DISCOUNT_DAY:
    print("No discount today! It costs: $" + "%0.2f" % book_price)
    

if book_price <= 128 and the_date == DISCOUNT_DAY:
                   book_price_eight = book_price
                   eight_discount = book_price_eight * 1.08
                   print("It costs $" + "%0.2f" % eight_discount)

elif book_price >= 128 and the_date == DISCOUNT_DAY:
                    book_price_sixteen = book_price
                    sixteen_discount = book_price_sixteen * 1.16
                    print("It costs $" + "%0.2f" % sixteen_discount)

