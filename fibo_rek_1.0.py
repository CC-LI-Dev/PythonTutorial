import time
import sys
#time start
start = time.time()
# def of variables
rek_list = [0,1,1]

# increasing of recursion limit
sys.setrecursionlimit(15000)
start = time.time()

#def of function
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
            
# function call and print
print(fib(10000, rek_list))
#print(rek_list)

#time end
end = time.time()
print("The time of execution of above program is :", end-start) 
