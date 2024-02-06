import math
import os
import string

emoticons = [":^) ", ":-] ", "=] ", ":] ", ":D "]

t = input("Möchtest du Buchstaben (B) oder Zahlen (Z) konvertieren?\n")

if t == "B":
    text = input("Gib die Buchstaben, die du konvertieren möchtest nun ein.\n")
    chars = list(text)
    output = ""
    for char in chars:
        if char.lower() not in string.ascii_lowercase:
            print("Es sind nur ASCII Zeichen erlaubt")
            break
        if char.isupper():
            output += ":)) "
        char = char.lower()

        index = string.ascii_lowercase.index(char)
        group = math.floor(index / 5)
        pos = index % 5

        if group == 6:
            output += ":-D "
        else:
            output = output + emoticons[group] + emoticons[pos]

    print(output)

elif t == "Z":
    zahl = input("Gib nun die Zahl, die du konvertieren möchtest ein\n")
    try:
        zahl = int(zahl)
    except Exception:
        print("Bitte gib nur Zahlen ein")
        exit()

    b = str(bin(zahl))
    if b.startswith("-"):
        b = b.replace("-", ":) ")
    else:
        b = ":( " + b

    b = b.replace("0b", "")
    b = b.replace("0", ":( ")
    b = b.replace("1", ":) ")

    print(b)

else:
    print("Bitte gib entweder B oder Z ein!")
    os.system("python converter.py")

os.system("pause")