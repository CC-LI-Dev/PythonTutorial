from random import *
wille = True
while wille == True:
    punkte = []

    pges = []


    print("Willkommen zu Kniffel - Mehrspieler ultra deluxe pro")
    print("Um deine Liste während des Spiels einzusehen, schreibe 'list'.")
    n = int(input("Wie viele Spieler?"))

    for j in range(n):
        pa = []
        for i in range(13):
            pa.append(False)
        punkte.append([])
        punkte[j] = pa
    

    def zug(n,punkte):
        
        #würfeln
        wurf =[]
        for i in range(5):
            zahl = randint(1,6)
            wurf.append(zahl)
        print("Dein Wurf: ", wurf)

        #wiederholen
        for j in range(2):
            for i in range(5):
                dumm = True
                while dumm == True:
                    print("Willst du die", wurf[i], "behalten? (j oder n?)")
                    wahl = str(input())
                    if wahl == "n":
                        wurf[i] = randint(1,6)
                        dumm = False
                    elif wahl == "j":
                        dumm = False
                    elif wahl == "list":
                        print(punkte[n-1])
                    else:
                        print("Das habe ich nicht verstanden. j oder n?")
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
            
            wertung = str(input("Als was möchtest du diesen Wurf werten? (zum streichen schreibe 'streich [kategorie]'"))

            #erster teil

            if wertung == "1er":
                if punkte[n-1][0] == False:
                    punkte[n-1][0] = wurf.count(1)*1
                    dumm = False
                else:
                    print("Das hast du schon.")
            elif wertung == "2er":
                if punkte[n-1][1] == False:
                    punkte[n-1][1] = wurf.count(2)*2
                    dumm = False
                else:
                    print("Das hast du schon.")
            elif wertung == "3er": 
                if punkte[n-1][2] == False:
                    punkte[n-1][2] = wurf.count(3)*3
                    dumm = False
                else:
                    print("Das hast du schon.")
            elif wertung == "4er": 
                if punkte[n-1][3] == False:
                    punkte[n-1][3] = wurf.count(4)*4
                    dumm = False
                else:
                    print("Das hast du schon.")
            elif wertung == "5er": 
                if punkte[n-1][4] == False:
                    punkte[n-1][4] = wurf.count(5)*5
                    dumm = False
                else:
                    print("Das hast du schon.")
            elif wertung == "6er":
                if punkte[n-1][5] == False:
                    punkte[n-1][5] = wurf.count(6)*6
                    dumm = False
                else:
                    print("Das hast du schon.")

            #zweiter teil

            elif wertung == "full house":
                if punkte[n-1][6] == False:
                    if (zahl1 == 3 or zahl2 == 3 or zahl3 == 3 or zahl4 == 3 or zahl5 == 3 or zahl6 == 3) and (zahl1 == 2 or zahl2 == 2 or zahl3 == 2 or zahl4 == 2 or zahl5 or zahl6 == 2):
                        punkte[n-1][6] = 25
                        dumm = False
                    else:
                        print("Das ist kein Full House. Depp.")
                else:
                    print("Das hast du schon.")

            elif wertung == "dreier pasch":
                if punkte[n-1][7] == False:
                    if (zahl1 >= 3 or zahl2 >= 3 or zahl3 >= 3 or zahl4 >= 3 or zahl5 >= 3 or zahl6 >= 3):
                        punkte[n-1][7] = sum(wurf)
                        dumm = False
                    else:
                        print("Das ist kein dreier Pasch. Depp.")
                else:
                    print("Das hast du schon.")

            elif wertung == "vierer pasch":
                if punkte[n-1][8] == False:
                    if (zahl1 >= 4 or zahl2 >= 4 or zahl3 >= 4 or zahl4 >= 4 or zahl5 >= 4 or zahl6 >= 4):
                        punkte[n-1][8] = sum(wurf)
                        dumm = False
                    else:
                        print("Das ist kein vierer Pasch. Depp.")
                else:
                    print("Das hast du schon.")

            elif wertung == "kleine straße":
                if punkte[n-1][9] == False: 
                    if wurfstr[3] == wurfstr[2]+1 == wurfstr[1]+2 == wurfstr[0]+3:
                        punkte[n-1][9] = 30
                        dumm = False
                    else:
                        print("Das ist keine kleine Straße. Depp.")
                else:
                    print("Das hast du schon.")

            elif wertung == "große straße":
                if punkte[n-1][10] == False:
                    if wurfstr[4] == wurfstr[3]+1 == wurfstr[2]+2 == wurfstr[1]+3 == wurfstr[0]+4:
                        punkte[n-1][10] = 40
                        dumm = False
                    else:
                        print("Das ist keine große Straße. Depp.")
                else:
                    print("Das hast du schon.")

            elif wertung == "kniffel":
                if punkte[n-1][11] == False:
                    if wurf[0] == wurf[1] == wurf[2] == wurf[3] == wurf[4]:
                        punkte[n-1][11] = 50
                        dumm = False
                    else:
                        print("Das ist kein Kniffel. Depp.")
                else:
                    print("Das hast du schon.")

            elif wertung == "chance":
                if punkte[n-1][12] == False:
                    punkte[n-1][12] = sum(wurf)
                    dumm = False
                else:
                    print("Das hast du schon.")

            elif wertung == "streich full house":
                if punkte[n-1][7] == False:
                    punkte[n-1][7] = 0
                    dumm = False
                else:
                    print("Das hast du schon.")

            elif wertung == "streich dreier pasch":
                if punkte[n-1][7] == False:
                    punkte[n-1][7] = 0
                    dumm = False
                else:
                    print("Das hast du schon.")

            elif wertung == "streich vierer pasch":
                if punkte[n-1][8] == False:
                    punkte[n-1][8] = 0
                    dumm = False
                else:
                    print("Das hast du schon.")

            elif wertung == "streich kleine straße":
                if punkte[n-1][9] == False:
                    punkte[n-1][9] = 0
                    dumm = False
                else:
                    print("Das hast du schon.")

            elif wertung == "streich große straße":
                if punkte[n-1][10] == False:
                    punkte[n-1][10] = 0
                    dumm = False
                else:
                    print("Das hast du schon.")

            elif wertung == "streich kniffel":
                if punkte[n-1][11] == False:
                    punkte[n-1][11] = 0
                    dumm = False
                else:
                    print("Das hast du schon.")

            elif wertung == "streich dreier pasch":
                if punkte[n-1][7] == False:
                    punkte[n-1][7] = 0
                    dumm = False
                else:
                    print("Das hast du schon.")
            
            elif wahl == "list":
                        print(punkte[n-1])

            else:
                print("Das kenne ich nicht.")
        
        print("Wurde notiert!")
        return(punkte)

    for i in range(13):
        for j in range(1,n+1):
            print("Spieler ",j, "ist dran!")
            punkte = zug(j,punkte)
            print("Nächster Spieler!")

    #auswertung

    for i in range(n):
        bonus = 0
        if sum(punkte[i][:6]) >= 63:
            bonus = 35
        pges.append(sum(punkte[i]) + bonus)
        
        print("Spieler ",i+1, "hat", pges[i], "Punkte erreicht!")

    winners = []
    psort = pges.sort()
    max = psort[:-1]

    for i in pges:
        if pges[i] == max:
            winners.append(i+1)
    if len(winners) == 1:
        print("Die gewinnende Person ist die spielende Person ", winners[0])
    else:
        print("Die gewinnenden Personen sind die spielenden Personen ", winners)
    
    dumm = True
    w = str(input("Noch mal? :D (ja oder nein?"))
    if w == "nein":
        wille = False
        dumm = False
    elif w == "ja":
        print("Richtige Entscheidung!! Auf ein neues :D")
        dumm = False
    else:
        print("Das habe ich leider nicht verstanden.")
