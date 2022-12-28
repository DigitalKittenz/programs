# kb day

# day = 10.24 october 24

LOW_DISCOUNT_MULTIPLIER = 1.08
HIGH_DISCOUNT_MULTIPLIER = 1.16
# discount = 0.08
# if price < 128

# discount = 0.16
# if price >= 128

day = str(input("Please enter the day"))

accepted_day_input = ["10.24", "October 24", "october 24", "1024", "10/24"]

spent = float(input("How much did it cost?"))

if day in accepted_day_input:
    if spent < 128:
        total_cost = spent * LOW_DISCOUNT_MULTIPLIER
        print(total_cost)
    elif spent == 0:
        print("You didn't buy anything")
    else:
        total_cost = spent * HIGH_COST_MULTIPLIER

if day not in accepted_day_input:
    print("wrong day, it costs: ", day)
