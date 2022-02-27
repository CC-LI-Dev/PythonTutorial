import random
test = "Der Mann geht nach Hause um sein Mittag einzunehmen. Er wird von seinem Hund begrüßt. Die Frau kommt etwas später von der Arbeit."
count = 0
letter = input("Geben sie einen Buchstaben zum Zählen an:")
letter_upper = letter.upper()
for j in test:
    if j == letter or j == letter_upper:
        count = count+1 
print(count)

count_word = 0
space = " "
test.strip()
test = test+" "

for k in test:
    if k == space:
        count_word = count_word+1

print(count_word)

output = []
userinput_list = []


def secretcode(userinput):
    j = 0
    userinput = userinput.replace(" ", "")
    for i in range(len(userinput)):
        userinput_list.append(userinput[i])
    for i in range(0, len(userinput_list)):
        if random.randint(1, 2) == 2:
            userinput_list.insert(i+j, " ")
        j = j+1
    output = "".join(userinput_list)        
    print(output)

secretcode(test)


