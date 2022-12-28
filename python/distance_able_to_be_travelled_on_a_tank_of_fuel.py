# Saraid Quinn
# KCOMPB_Y1
# WEEK 3/4 Example problem -> (km of travel) per (gallon of fuel)



# WHEN fuel tank = 60L
# AND fuel consumption = 14km/L

# REF:  1 gallon = 4.55L

# 1: Distance able to be travelled on one tank of fuel?
# 2: How many litres to travel 650km?
# 3: how many times to refuel, to travel 2000km?
# 4: How many KM can be travel using 10 gallons of fuel in the same car?


#############################################################################
FUEL_TANK_CAPACITY = 60 

kmTravelledPerLitre = 14
litresUsedPerKm = 1 / kmTravelledPerLitre

print(f"Your fuel tank capacity is {FUEL_TANK_CAPACITY}, km travelled per litre is {kmTravelledPerLitre} and litres used per km is {litresUsedPerKm:.2f}")

change_initial_values = input("Do you wish to change any of these values?\nType F to change Fuel Tank Capacity\nType K to change km travelled per litre\\n type FK to change both\nType ENTER to disregard.")
if change_initial_values == "F":
    FUEL_TANK_CAPACITY = float(input("Fuel Tank Capacity\t:"))
elif change_initial_values == "K":
    kmTravelledPerLitre = float(input("KM Travelled Per Litre"))
elif change_initial_values == "FK":
    FUEL_TANK_CAPACITY = float(input("Fuel Tank Capacity\t:")) 
    kmTravelledPerLitre = float(input("KM Travelled Per Litre"))

print(f"Your fuel tank capacity is {FUEL_TANK_CAPACITY}, km travelled per litre is {kmTravelledPerLitre} and litres used per km is {litresUsedPerKm:.2f}")



# 1 Distance travelled on one tank of fuel
distanceOnOneTank = FUEL_TANK_CAPACITY / kmTravelledPerLitre
print(f"Q1. Distance able to be travelled on one tank of fuel is = {distanceOnOneTank:.2f}","km." )

# 2 Litres to travel 650KM
distance = 650
sixFiftyDistance = litresUsedPerKm * distance
print(f"Q2. Litres needed to travel 650KM is = {sixFiftyDistance:.2f}","Litres")

# 3 How many times do you need to refuel to travel 2000km?

distance = 2000

twoKLitres = litresUsedPerKm * distance

pitstopsPerTank = litresUsedPerKm * FUEL_TANK_CAPACITY

import math
pitstopsPerTwoK = math.ceil(twoKLitres / FUEL_TANK_CAPACITY)

print(f"Q3. Litres needed to travel 2000km is = {twoKLitres:.2f}"+"L with " + str(pitstopsPerTwoK) + " refuels")

# 4 How many km can be travelled using 10 gallons of fuel?
GALLON = 4.55 

# How many km with 10 gallons?

litresInTenGallons = GALLON * 10
# we used 45 litres here
kmTravelled = litresInTenGallons * kmTravelledPerLitre
print(kmTravelled)

print(f"Q4. We can travel {kmTravelled:.2f}", "km with 10 gallons")







