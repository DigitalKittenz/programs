
# working out
### second rate calculation ###

##################            690  -      240         =450
#  690 - 540 = 150
# (690 - 150)- 240
# ==== (540) - 240 = 300

# next rate 540 - first rate 240 = 300 * next_hourly_cost 0.13
# 

# 300 is the amt to multiply
#########################################################################

# ASK the user: how many kWh units have you used in the past
#                                                           2 MONTHS
# OUTPUT: total charge according to the constant rates.

# first 240 kWh: 14c per kWh
# next 300 kWh: 13c per kWh
# over 540 kWh: 11c per kWh


# extra mod: account for invalid input.

##############################################################################

FIRST_ELECTRICITY_LIMIT = 240
FIRST_HOURLY_COST = 0.14
entire_first_rate_sum = FIRST_ELECTRICITY_LIMIT * FIRST_HOURLY_COST
# 33.6

NEXT_ELECTRICITY_LIMIT = 540
NEXT_HOURLY_COST = 0.13
entire_next_rate_sum = (NEXT_ELECTRICITY_LIMIT - FIRST_ELECTRICITY_LIMIT) * NEXT_HOURLY_COST
# 39

HIGH_HOURLY_COST = 0.11


electricity_used = float(input("How many kWh units have you used in the past 2 months?"))

# equations

first_rate_calculation = electricity_used * FIRST_HOURLY_COST

next_rate_electricity_used = FIRST_ELECTRICITY_LIMIT * FIRST_HOURLY_COST

next_rate_calculation = (NEXT_ELECTRICITY_LIMIT - FIRST_ELECTRICITY_LIMIT) * NEXT_HOURLY_COST

high_rate_calculation = (electricity_used - NEXT_ELECTRICITY_LIMIT) * 0.11

# calculations

total_charge_output = "Your total charge is: €"

### less than or equal to 240
if electricity_used <= 240:
    print(total_charge_output,"%0.2f" % first_rate_calculation)
    
# greater than 240 and less than or equal to 540
elif electricity_used > 240 and electricity_used <= 540:
    print(total_charge_output,"%0.2f" % next_rate_calculation)
    
elif electricity_used > 540:
    five_forty_sum = (entire_first_rate_sum + entire_next_rate_sum) + high_rate_calculation
    print(total_charge_output, "%0.2f" % five_forty_sum)
