import sys

alphabet = "qwertzuiopüasdfghjklöäyxcvbnmQWERTZUIOPÜASDFGHJKLÖÄYXCVBNM"


def sarcasmify(strInput):
    listinput = list(strInput)
    big = True
    counter = 0
    for char in listinput:
        if char in alphabet:
            if big:
                listinput[counter] = char.upper()
                big = False
            else:
                listinput[counter] = char.lower()
                big = True
        counter += 1

    return "".join(listinput)