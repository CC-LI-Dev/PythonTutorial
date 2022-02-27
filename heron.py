num = float(input("Zahl:"))
com = int(input("Auf wieviel Stellen nach dem Komma soll gerundet werden:"))
a = 1
int(a)
b = num
while True:
    if round(a, com)-round(b, com) == 0:
        print(round(a,com))
        break
    a = (a+b)/2
    b = num/a
    print(a, b)
