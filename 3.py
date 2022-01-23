x = 1.0
while True:
    if x != 11:
        print(x)
        x = x+1
    else:
        break


summe = 0
durchschnitt = 0

anzahlschueler = int(input("Schülerzahl in Klasse 5a:"))

for i in range(1, anzahlschueler+1):
    print("Note Schueler", i, ":")
    Note = int(input())
    summe = summe + Note

durchschnitt = summe / anzahlschueler
print("Der Notendurchschnitt beträgt:", durchschnitt)

