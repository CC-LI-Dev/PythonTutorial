#Verzweigungen

#zweiseitige Verzweigung
a = int(input("Geben sie eine Zahl a ein:"))
b = int(input("Geben sie b ungleich a ein:"))

if a < b:
    print("a ist kleiner als b.")
else:
    print("a ist größer als b.")

#einseitige Verzweigung

if a < 0:
    a = -a
if b < 0:
    b = -b

print(a, b)

#mehrseitige Verzweigung

note = int(input("Note?"))
if note == 1:
    print("sehr gut")
elif note == 2:
    print("gut")
elif note == 3:
    print("befriedigend")
elif note == 4:
    print("ausreichend")
elif note == 5:
    print("mangelhaft")
elif note == 6:
    print("ungenügend")
else:
    print("keine gültige Note")