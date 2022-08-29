userinput = input("Geben sie ein/en Satz/Wort ohne Punkt zur Überprüfung ein:")
userinput = userinput.replace(" ", "")
userinput = userinput.lower()
userinput_rev = userinput[::-1]
if userinput == userinput_rev:
    print("Der/Das Satz/Wort ist ein Palindrom.")