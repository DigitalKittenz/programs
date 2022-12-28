
KM = 1.61


calculation_choice = str(input("What do you want to calculate? Mile or KM?"))

sums = int(input(f"How many {calculation_choice} sums?"))

while sums > 0:
    if str("mile") or str("both")in calculation_choice:
        mile = float(input("Miles-->"))
        mile_calculation = mile * KM
        sums -= 1
        print("%0.2f"% mile_calculation + str("km"))
    elif str("km") or str("both") in calculation_choice:
        km = float(input("km-->"))
        km_calculation = km / KM
        sums -= 1
        print("%0.2f"% km_calculation + str("km"))
    elif str("both") in calculation_choice:
        km = float(input("km-->"))
        km_calculation = km / KM
        print("%0.2f"% km_calculation + str("km"))

else:
    print("end")


