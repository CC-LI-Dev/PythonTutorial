import time
start = time.time()
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(200))

end = time.time()

print("The time of execution of above program is :", end-start)
