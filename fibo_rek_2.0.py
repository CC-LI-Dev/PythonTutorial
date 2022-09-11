import time
start = time.time()

def fib(n, rek_list=[]):
  if n == 0:
    return rek_list

  if len(rek_list) < 2:
    return fib(n-1, rek_list + [1])

  return fib(n-1, rek_list + [rek_list[-1] + rek_list[-2]])

print(fib(200)[-1])

end = time.time()

print("The time of execution of above program is :", end-start)