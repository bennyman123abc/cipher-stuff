import string
import random

alphlist = list(string.ascii_lowercase)
alphdict = {}

def main():
    global alphdict
    alphdict = {}
    for c in alphlist:
        if not c in alphdict:
            gen_letter(c)
        print("{} = {}".format(c.upper(), alphdict[c].upper()))
    serial = cipher("cipher").upper()
    print(serial)
    f = open(serial + "-dict.txt", "w")
    f.write(str(alphdict))
    f.close()

    f = open(serial + ".txt", "w")
    for c in alphlist:
        f.write("{} = {}\n".format(c.upper(), alphdict[c].upper()))
    f.close()

def gen_letter(letter):
    # make sure we aren't inserting duplicates
    if letter in alphdict:
        return
    n = alphlist[random.randint(0, len(alphlist) - 1) - 1]
    if n in alphdict:
        gen_letter(letter) # restart because we'll be duplicating if we don't
        return
    alphdict[letter] = n
    alphdict[n] = letter

def cipher(text):
    s = ""
    for c in text:
        s += alphdict[c]
    return s

for _ in range(0, 1):
    main()
