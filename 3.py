num = input("Geben Sie eine Zahl ein:")
def checksum_calc(num):
    checksum = sum([int(i) for i in num])
    return checksum
print(checksum_calc(num))