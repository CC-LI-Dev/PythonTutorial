number = 100000
palindrome_list = []
while number < 999999:
    number_case1 = number+1
    number_case2 = number+2
    number_case3 = number+3
    number_str_origin = str(number)
    number_str_case1 = str(number_case1)
    number_str_case2 = str(number_case2)
    number_str_case3 = str(number_case3)
    if number_str_origin[5:1:-1] == number_str_origin[2:6] and number_str_case1[5:0:-1] == number_str_case1[1:6] and number_str_case2[4:0:-1] == number_str_case2[1:5] and number_str_case3[::-1] == number_str_case3:
        palindrome_list.append(number_str_origin)
        number = number+1
    else:
        number = number+1
    
print(palindrome_list)