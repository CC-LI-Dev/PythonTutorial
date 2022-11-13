feld2 = [1, 3, 7, 12, 14, 18, 19, 21, 23, 35]
key = 21
links = 0
rechts = len(feld2)
def bin_search(feld, key):
    global links
    global rechts
    stelle = -1
    while stelle != key:
        mitte = (rechts+links)//2

        if key == feld[mitte]:
            return mitte
        elif key < feld[mitte]:
            rechts = mitte
        else:            
            links = mitte + 1

        if rechts == links:
            stelle = None
            return stelle

print(bin_search(feld2, 1))
