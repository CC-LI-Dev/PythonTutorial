
def rek(n):
    print("Es war ein mal ein Vater, der hatte ", n," Söhne und er erzählte: ")
    if n == 0:
        print("Papa ist traurig.") #direkter Fall
        
    else:
        rek(n-1) # Rekusrsionsabstieg 
    print("...und wenn sie nicht gestorben sind...") #Rekursionsaufstieg 
    
    
    
        
    #rek(n-1)
rek(7)


def fak(n):
    if n == 0:
        return 1
    else:
        return fak(n-1)*n
print(fak(5))
