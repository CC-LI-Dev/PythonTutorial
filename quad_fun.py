import math
#pq - Formel

def pq(p, q):
    if disk > 0:
        x1 = -p/2 + math.sqrt(disk)
        x2 = -p/2 - math.sqrt(disk)
    elif disk == 0:
        x1 = -p/2 
        x2 = None
    else:
        x1 = None
        x2 = None
    return (x1, x2)
while True:
    p = float(input("Geben sie p an:"))
    q = float(input("Geben sie q an:"))
    disk = (p**2/4)-q
    print(pq(p, q))
