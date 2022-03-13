# initialisation of output list

palindrome_list = []

# main loop

for i in range(1, 999999):

    # creation of cases 1-3 & conversion from int to str

    number_case1 = i+1
    number_case2 = i+2
    number_case3 = i+3
    number_str_origin = str(i)
    number_str_origin = number_str_origin.zfill(6)
    number_str_case1 = str(number_case1)
    number_str_case1 = number_str_case1.zfill(6)
    number_str_case2 = str(number_case2)
    number_str_case2 = number_str_case2.zfill(6)
    number_str_case3 = str(number_case3)
    number_str_case3 = number_str_case3.zfill(6)

    # testing of numbers & adding results into list

    if number_str_origin[5:1:-1] == number_str_origin[2:6]:
        if number_str_case1[5:0:-1] == number_str_case1[1:6]:
            if number_str_case2[4:0:-1] == number_str_case2[1:5]:
                if number_str_case3[::-1] == number_str_case3:
                    palindrome_list.append(number_str_origin)
    
    
# output

print("Possible palindromes are:",palindrome_list)
