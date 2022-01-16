# year input
year = int(input("Geben sie ein Jahr ein:"))

# calculation

if year % 4 == 0 and year > 1582:
    if year % 100 == 0 and year % 400 == 0:
        print(year, "ist ein Schaltjahr.")
    elif year % 100 == 0 and year % 400 != 0:
        print(year, "ist kein Schaltjahr.")
    elif year % 4 == 0 and year % 100 == 0:
        print(year, "ist kein Schaltjahr.")
    elif year % 4 == 0 and year % 100 != 0:
        print(year, "ist ein Schaltjahr.")
else:
    print(year, "ist kein Schaltjahr.")
        