number = 198888
number_int_origin = str(number)
number_case1 = number+3
number_str_case1 = str(number_case1)
print(number_int_origin, number_int_origin[::-1], number_int_origin[5:0:-1], number_int_origin[1:6])
print(number_str_case1[::-1], number_str_case1)
if number_str_case1[::-1] == number_str_case1:
    print("OK")
