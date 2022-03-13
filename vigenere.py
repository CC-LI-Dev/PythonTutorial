# variables
key = input("Geben sie ihren Key an:")
text = input("Geben sie ihren Klartext an:")
alphabet = ["_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
encoded_text = []

# formatting of input
text_list = text.split()
text = "".join(text_list)
text = text.lower()

# redefintion of key

key = key*len(text)
key = key[:len(text)]

for i in range(len(text)):
    sorted_list = alphabet
    index_text = alphabet.index(text[i])
    index_key = alphabet.index(key[i])
    for j in range(1, index_key):
        swap = sorted_list.pop(1)
        sorted_list.append(swap)
    index_key = sorted_list.index(key[i])
    encoded_text.append(sorted_list[index_key+index_text-1])
    index_key = 0
    index_text = 0


print(encoded_text)