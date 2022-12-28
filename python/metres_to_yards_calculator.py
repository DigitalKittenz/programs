#INPUT distance in yards.
#Then convert it to metres. 2 decimal places.


YARD = 0.9144

metre = float(input("Enter metres: "))

metreToYard = metre / 0.9144

print(f"{metre:.2f}", f"metres is equal to {metreToYard:.2f}", "yards.")
