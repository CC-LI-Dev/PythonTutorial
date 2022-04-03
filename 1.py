from cProfile import run


hi_num = int(input("Geben Sie die höchste Zahl (numerisch) an:"))
num_list = []
run = 2
for i in range(2, hi_num):
	num_list.append(i+1)
while run < hi_num:
    num_list = [item for item in num_list if item % run != 0 or item == run]
    run = run+1
print(num_list)



