import time
import sys
start = time.time()

rek_list = [0,1,1]
sys.setrecursionlimit(15000)
start = time.time()


def fib(n, rek_list):
    
    if n <= 2:
        return 1
    else:
        if len(rek_list) == n+2:
            return rek_list[n]
        else:
            x = fib(n-1, rek_list)+fib(n-2, rek_list)
            rek_list.append(x)
            return x
            
print(fib(10000, rek_list))

end = time.time()

print("The time of execution of above program is :", end-start)
