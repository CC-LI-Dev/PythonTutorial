from random import *
birthd = []
doubles = 0
a = 100000
occurences = 0

for i in range(1, a):
    for j in range(0, 23):
        birthd.append(randint(0, 365))
    for k in range(0, 365):
        if birthd.count(k) > 1:
            doubles = doubles+1
    if doubles > 0:
        occurences = occurences+1
    birthd.clear()

probability = occurences/a
print(probability)