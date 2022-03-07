number = 100000
palindrome_list = []
while number < 999999:
    if str(number)[5:1:-1] == str(number)[2:6]:
        if str(number+1)[5:0:-1] == str(number+1)[1:6]:
            if str(number+2)[4:0:-1] == str(number+2)[1:5]:
                if str(number+3)[::-1] == str(number+3):
                    palindrome_list.append(number)
                    number = number+1
                else:
                    number = number+1 
            else:
                number = number+1
        else:
            number = number+1
    else:
        number = number+1
    
print(palindrome_list)
