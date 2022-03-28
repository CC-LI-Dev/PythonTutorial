hi_num = int(input("Geben Sie die höchste Zahl (numerisch) an:"))
num_list = []
mult = 0
run_co = 0
n = 1
small_primes = [2, 3, 5, 7, 11, 13, 17, 19]

def list_removal(list, test_item):
    return [item for item in list if item != test_item]

for i in range(hi_num):
    num_list.append(i+1)

for i in small_primes:
    while mult <= hi_num and run_co <= hi_num:
        mult = i * n
        num_list = list_removal(num_list, mult)
        n = n+1
    n = 1
    mult = 0
    run_co = run_co+1
print(num_list)


