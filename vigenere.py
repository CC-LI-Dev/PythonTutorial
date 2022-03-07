# variables
key = input("Geben sie ihren Key an:")
text = input("Geben sie ihren Klartext an:")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# formatting of input
text_list = text.split()
text = "".join(text_list)
text = text.lower()

# redefintion of key

key = key*len(text)
key = key[:len(text)]

