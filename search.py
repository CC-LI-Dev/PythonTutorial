feld1 = [23, 12 , 21, 35 ,14, 1, 3, 19, 7, 18, 21]
feld2 = [1, 3, 7, 12, 14, 18, 19, 21, 23, 35]

#Funktion Sequentielle Suche
def seq_search(key, feld):
    i = 0
    stelle = -1 #Element noch nicht gefunden
    #stelle = feld.index(key)    
    while stelle == -1 and i < len(feld):    
        if key == feld[i]:
            stelle = i
        i = i+1
    return stelle

#Funktion binäre Suche

#Main
print(seq_search(23, feld1))

