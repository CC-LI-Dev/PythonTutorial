import time
start = time.time()
rek_list = []
def fib(n, rek_list):
    if n <= 2:
        return 1
    else:
        if len(rek_list) == n:
            return rek_list[n-1]
        else:
            x = fib(n-1, rek_list)+fib(n-2, rek_list)
            rek_list.append(x)
            return x
            
print(fib(200, rek_list))

end = time.time()

print("The time of execution of above program is :", end-start)
