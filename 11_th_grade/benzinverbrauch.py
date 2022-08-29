distdriven = float(input("Fahrstrecke:"))
fuelamount = float(input("Nachgetankte Menge:"))
quotient = 100/distdriven
usa_per_hun = fuelamount*quotient
print("Ihr Verbrauch in 100km ist", usa_per_hun, "Liter.")