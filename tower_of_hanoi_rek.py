A = []
B = []
C = []
n = 3
for i in range(n):
    A.append(i)

def hanoi(n, A, B, C):
    move1 = A.pop(0)
    C = C.insert(0, move1)
    
    