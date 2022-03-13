# variables
key = input("Geben sie ihren Key ein:")
text = input("Geben sie ihren Klartext ein:")
alphabet = ["_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet2 = ["_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
encoded_text_list = []
decoded_text_list = []

# formatting of input
text_list = text.split()
text = "".join(text_list)
text = text.lower()

key_list = key.split()
key = "".join(key_list)
key = key.lower()

# redefintion of key

key = key*len(text)
key = key[:len(text)]

# encoding through Vigenere

for i in range(len(text)):
    
    index_text = alphabet2.index(text[i])
    index_key = alphabet.index(key[i])
    for j in range(1, index_key):
        swap = alphabet.pop(1)
        alphabet.append(swap)
    encoded_text_list.append(alphabet[index_text])

# output of encoded text

encoded_text = "".join(encoded_text_list)
print("Der kodierte Text ist:", encoded_text)

# input of encoded text

key_encoded = input("Geben sie ihren Key ein:")
input_encoded_text = input("Geben sie ihren kodierten Text ein:")

# redefintion of key

key_encoded = key_encoded*len(text)
key_encoded = key_encoded[:len(text)]

# decoding

for i in range(len(input_encoded_text)):
    
    index_key_encoded = alphabet.index(key_encoded[i])
    for j in range(1, index_key_encoded):
        swap = alphabet.pop(1)
        alphabet.append(swap)
    index_input_encoded = alphabet.index(input_encoded_text[i])
    decoded_text_list.append(alphabet2[index_input_encoded])

# output of decoded text
decoded_text = "".join(decoded_text_list)
print("Der dekodierte Text ist:", decoded_text)
    
    
