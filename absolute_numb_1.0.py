import time

# number and count definition
number = 0
n = 1
abs_add = 0
list_abs_number = []
end_time = float(input("How many seconds to run?"))
start_time = time.time()

# process of dividing to find absolute numbers
def process(number):
        n = 1
        abs_add = 0
        while n < number:
            if number % n == 0:
                abs_add = abs_add+n
            n = n + 1
        if abs_add == number:
            list_abs_number.append(number)
    
while time.time() - start_time <= end_time:
    number = number + 1
    process(number)

# output
print(list_abs_number)
