limit = int(input("Geben Sie die höchste Zahl (numerisch) an:"))
list = range(2, limit + 1)
divider = 2
while divider < limit:
    list = [item for item in list if item == divider or item % divider != 0]
    divider += 1
print(list)