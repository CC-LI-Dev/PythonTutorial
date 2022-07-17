from array import array
from random import *


einer = False
zweier = False
dreier = False
vierer = False
fünfer = False
sechser = False

dreierp = False
viererp = False
fullhouse = False
grstr = False
klstr = False
kniffel = False
chance = False

p1 = 0
p2 = 0
pges = 0

#HA

for k in range(13):
    
    #würfeln
    wurf =[]
    for i in range(5):
        zahl = randint(1,6)
        wurf.append(zahl)
    print("Dein Wurf: ", wurf)

    #wiederholen
    for j in range(2):
        for i in range(5):
            print("Willst du die", wurf[i], "behalten? (ja oder nein?)")
            wahl = str(input())
            if wahl == "nein":
                wurf[i] = randint(1,6)
        print("Neuer Wurf: ", wurf)
    
    #wertung

    wurf.sort() # Funktioniert bei dir nur mit wurf = wurf.sort()

    zahl1 = wurf.count(1)
    zahl2 = wurf.count(2)
    zahl3 = wurf.count(3)
    zahl4 = wurf.count(4)
    zahl5 = wurf.count(5)
    zahl6 = wurf.count(6)
    
    wurfstr = []
    for i in wurf:
        if i not in wurfstr:
            wurfstr.append(i)

    dumm = True
    while dumm == True:
        
        wertung = str(input("Als was möchtest du diesen Wurf werten?"))

        #erster teil

        if wertung == "1er":
            if einer == False:
                p1 = p1 + wurf.count(1)*1
                einer = True
                dumm = False
            else:
                print("Das hast du schon.")
        elif wertung == "2er":
            if zweier == False:
                p1 = p1 + wurf.count(2)*2
                zweier = True
                dumm = False
            else:
                print("Das hast du schon.")
        elif wertung == "3er": 
            if dreier == False:
                p1 = p1 + wurf.count(3)*3
                dreier = True
                dumm = False
            else:
                print("Das hast du schon.")
        elif wertung == "4er": 
            if vierer == False:
                p1 = p1 + wurf.count(4)*4
                vierer = True
                dumm = False
            else:
                print("Das hast du schon.")
        elif wertung == "5er": 
            if fünfer == False:
                p1 = p1 + wurf.count(5)*5
                fünfer = True
                dumm = False
            else:
                print("Das hast du schon.")
        elif wertung == "6er":
            if sechser == False:
                p1 = p1 + wurf.count(6)*6
                sechser = True
                dumm = False
            else:
                print("Das hast du schon.")

        #zweiter teil

        elif wertung == "full house":
            if fullhouse == False:
                if (zahl1 == 3 or zahl2 == 3 or zahl3 == 3 or zahl4 == 3 or zahl5 == 3 or zahl6 == 3) and (zahl1 == 2 or zahl2 == 2 or zahl3 == 2 or zahl4 == 2 or zahl5 or zahl6 == 2):
                    p2 == p2 + 25
                    fullhouse = True
                    dumm = False
                else:
                    print("Das ist kein Full House. Depp.")
            else:
                print("Das hast du schon.")

        elif wertung == "dreier pasch":
            if dreierp == False:
                if (zahl1 >= 3 or zahl2 >= 3 or zahl3 >= 3 or zahl4 >= 3 or zahl5 >= 3 or zahl6 >= 3):
                    p2 == p2 + sum(wurf)
                    dreierp = True
                    dumm = False
                else:
                    print("Das ist kein dreier Pasch. Depp.")
            else:
                print("Das hast du schon.")

        elif wertung == "vierer pasch":
            if viererp == False:
                if (zahl1 >= 4 or zahl2 >= 4 or zahl3 >= 4 or zahl4 >= 4 or zahl5 >= 4 or zahl6 >= 4):
                    p2 == p2 + sum(wurf)
                    viererp = True
                    dumm = False
                else:
                    print("Das ist kein vierer Pasch. Depp.")
            else:
                print("Das hast du schon.")

        elif wertung == "kleine straße":
            if klstr == False: 
                if wurfstr[3] == wurfstr[2]+1 == wurfstr[1]+2 == wurfstr[0]+3:
                    p2 == p2 + 30
                    klstr = True
                    dumm = False
                else:
                    print("Das ist keine kleine Straße. Depp.")
            else:
                print("Das hast du schon.")

        elif wertung == "große straße":
            if grstr == False: 
                if wurfstr[4] == wurfstr[3]+1 == wurfstr[2]+2 == wurfstr[1]+3 == wurfstr[0]+4:
                    p2 == p2 + 40
                    grstr = True
                    dumm = False
                else:
                    print("Das ist keine große Straße. Depp.")
            else:
                print("Das hast du schon.")

        elif wertung == "kniffel":
            if kniffel == False:
                if wurf[0] == wurf[1] == wurf[2] == wurf[3] == wurf[4]:
                    p2 == p2 + 50
                    kniffel = True
                    dumm = False
                else:
                    print("Das ist kein Kniffel. Depp.")
            else:
                print("Das hast du schon.")

        elif wertung == "chance":
            if chance == False:
                p2 = p2 + sum(wurf)
                chance = True
                dumm = False
            else:
                print("Das hast du schon.")
        else:
            print("Das kenne ich nicht.")
    
    print("Wurde notiert!")

if p1 >= 63:
    p1 = p1 + 35
pges = p1 + p2

print(pges)