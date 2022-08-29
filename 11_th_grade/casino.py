failedattempts = 0
password = input("Geben sie das Passwort ein:")
while failedattempts <= 2 and password != "Liborius":
    password = input("Geben sie das Passwort ein:")
    if password != "Liborius":
        failedattempts = failedattempts+1

if password == "Liborius":
    print("Zugriff zugelassen.")
elif failedattempts == 3:
    print("Zugriff nicht authorisiert!")