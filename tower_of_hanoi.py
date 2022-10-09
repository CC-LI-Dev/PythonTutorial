A = []
B = []
C = []
for i in range(3):
    A.append(i)

def hanoi(A, B, C):
    repick_take = True
    repick_place = False
    move_disk = None
    print(A)
    print(B)
    print(C)
    while repick_take == True:
        take_disk = input("Von welchem Turm entfernen? (A,B,C)")
        if take_disk == "A":
            print(A[0])
        elif take_disk == "B":
            print(B[0])
        elif take_disk == "C":
            print(C[0])
        repick_take = bool(int(input("Wollen Sie neu wählen? (1,0)")))
        if repick_take == False:
            if take_disk == "A":
                move_disk == A.pop(0)
            elif take_disk == "B":
                move_disk == B.pop(0)
            elif take_disk == "C":
                move_disk == C.pop(0)

    while repick_place == False:
        place_disk = input("Auf welchen Turm legen? (A,B,C)")
        if place_disk == "A":
            if 
    
