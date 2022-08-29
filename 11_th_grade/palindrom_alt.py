# initialisation of output list

palindrome_list = []

# main loop

for i in range(1, 999999):
    # testing of cases
    if str(i).zfill(6)[5:1:-1] == str(i).zfill(6)[2:6] and str(i+1).zfill(6)[5:0:-1] == str(i+1).zfill(6)[1:6] and str(i+2).zfill(6)[4:0:-1] == str(i+2).zfill(6)[1:5] and str(i+3).zfill(6)[::-1] == str(i+3).zfill(6):
        palindrome_list.append(i)
    
# output

print("Possible palindromes are:", palindrome_list)
