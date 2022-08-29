import random
k = 1000000000
countGlobalam = 0
j = 100
l = 0
countGlobal = 0
while k > 0:
    while j > 0:
        count = 0
        i = 3
        guess = 3
        
        while i > 0:
            ranNum = random.randint(1,6)
            if ranNum == guess:
                count = count+1
            i = i-1
        if count > 0:
            countGlobal = countGlobal+1
        j = j-1
    countGlobalam = countGlobalam+countGlobal
    k = k-1
    l = l+1
print("Durschnittswahrscheinlichkeit:", countGlobalam/l)