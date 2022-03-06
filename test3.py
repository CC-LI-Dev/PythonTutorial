number = 198891
palindrome_list = []

number_case1 = number+1
    
number_str_origin = str(number)
number_str_case1 = str(number_case1)
print(number_str_origin[::-1], number_str_origin)  
if number_str_origin[::-1] == number_str_origin:
    print("OK")

palindrome_list.append(number_case1)
print(palindrome_list)