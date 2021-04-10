import json

# laadt de bigrammen en trigrammen in
with open('Bigrammen.txt', 'r') as f:
    bigrammen = json.loads(f.read())

with open('Trigrammen.txt', 'r') as g:
    trigrammen = json.loads(g.read())

# Stap 1: de herkenner haalt uit de zin alle bigrammen en trigrammen
zin = str(input("Voer een zin in in het spaans/nederlands/engels/fins/frans/duits: \n"))
woorden = zin.split(" ")
charlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "ä", "Ä", "à", "À", "á", "Á", "â", "Â", "å", "Å", "ã", "Ã", "æ", "Æ", "Ç", "ü", "é", "ç", "ê", "ë", "è", "ï", "î", "ì", "ô", "ö", "ò", "û", "ù", "ÿ", "¢", "í", "ó", "ú", "ñ", "Ñ", "ß", "µ", "Š", "š", "œ", "Ÿ", "È", "É", "Ê", "Ë", "Ì", "Í", "Î", "Ï", "Ð", "Ò", "Ó", "Ô", "Õ", "Ö", "Ø", "Ù", "Ú", "Û", "Ü", "Ý", "õ", "ø", "ü", "ý"]
kanslist = []

for woord in woorden:
    if len(woord) > 3:
        # filter alle rare characters
        newwoord = str(woord)
        for letter in range(len(woord)):
            if woord[letter] not in charlist:
                if letter == len(woord):
                    newwoord = newwoord[0:letter:]
                else:
                    newwoord = newwoord[0:letter:] + woord[letter + 1::]
        woord = newwoord

        trigramlist = []
        bigramlist = []

        # trigrammen en (tussen)bigrammen
        for letter in range(len(woord) - 2):
            trigram = woord[letter:letter + 3]
            trigramlist.append(trigram)

            if letter != 0:  # want het eerste bigram is geen tussen-bigram
                bigram = woord[letter:letter + 2]
                bigramlist.append(bigram)

        # Stap 2: en vergelijkt deze met de kansen van de talen
        kansen = []

        for trigram in trigramlist:
            minchance = 0.1 / trigrammen[0]
            # zoek het trigram in de grote lijst
            encountered = False
            for counter in range(1, len(trigrammen)):
                if trigrammen[counter][0] == trigram:
                    encountered = True
                    if not kansen:  # als kansen leeg is
                        kansen.append([
                            trigrammen[counter][1] / trigrammen[0],
                            trigrammen[counter][2] / trigrammen[0],
                            trigrammen[counter][3] / trigrammen[0],
                            trigrammen[counter][4] / trigrammen[0],
                            trigrammen[counter][5] / trigrammen[0],
                            trigrammen[counter][6] / trigrammen[0]
                        ])
                    else:
                        kansen[0][0] = kansen[0][0] * (trigrammen[counter][1] / trigrammen[0])
                        kansen[0][1] = kansen[0][1] * (trigrammen[counter][2] / trigrammen[0])
                        kansen[0][2] = kansen[0][2] * (trigrammen[counter][3] / trigrammen[0])
                        kansen[0][3] = kansen[0][3] * (trigrammen[counter][4] / trigrammen[0])
                        kansen[0][4] = kansen[0][4] * (trigrammen[counter][5] / trigrammen[0])
                        kansen[0][5] = kansen[0][5] * (trigrammen[counter][6] / trigrammen[0])

            if not encountered:
                minchance = 0.1 / trigrammen[0]
                trigrammen[0] += 0.6
                trigrammen.append(
                    [trigram, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, minchance, minchance, minchance, minchance, minchance,
                     minchance])
                if not kansen:  # als kansen leeg is
                    kansen.append([
                        minchance,
                        minchance,
                        minchance,
                        minchance,
                        minchance,
                        minchance
                    ])
                else:
                    kansen[0][0] = kansen[0][0] * minchance
                    kansen[0][1] = kansen[0][1] * minchance
                    kansen[0][2] = kansen[0][2] * minchance
                    kansen[0][3] = kansen[0][3] * minchance
                    kansen[0][4] = kansen[0][4] * minchance
                    kansen[0][5] = kansen[0][5] * minchance

        for bigram in bigramlist:
            minchance = 0.1 / bigrammen[0]
            # zoek het bigram in de grote lijst
            encountered = False
            for counter in range(1, len(bigrammen)):
                if bigrammen[counter][0] == bigram:
                    encountered = True
                    if len(kansen) == 1:  # als alleen maar de trigram kansen ingevuld zijn
                        kansen.append([
                            bigrammen[counter][1] / bigrammen[0],
                            bigrammen[counter][2] / bigrammen[0],
                            bigrammen[counter][3] / bigrammen[0],
                            bigrammen[counter][4] / bigrammen[0],
                            bigrammen[counter][5] / bigrammen[0],
                            bigrammen[counter][6] / bigrammen[0]
                        ])
                    else:
                        kansen[1][0] = kansen[1][0] * (bigrammen[counter][1] / bigrammen[0])
                        kansen[1][1] = kansen[1][1] * (bigrammen[counter][2] / bigrammen[0])
                        kansen[1][2] = kansen[1][2] * (bigrammen[counter][3] / bigrammen[0])
                        kansen[1][3] = kansen[1][3] * (bigrammen[counter][4] / bigrammen[0])
                        kansen[1][4] = kansen[1][4] * (bigrammen[counter][5] / bigrammen[0])
                        kansen[1][5] = kansen[1][5] * (bigrammen[counter][6] / bigrammen[0])

            if not encountered:
                bigrammen[0] += 0.6
                minchance = 0.1 / bigrammen[0]
                bigrammen.append(
                    [bigram, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, minchance, minchance, minchance, minchance, minchance,
                     minchance])
                if len(kansen) == 1:  # als alleen maar de trigram kansen ingevuld zijn
                    kansen.append([
                        minchance,
                        minchance,
                        minchance,
                        minchance,
                        minchance,
                        minchance
                    ])
                else:
                    kansen[1][0] = kansen[1][0] * minchance
                    kansen[1][1] = kansen[1][1] * minchance
                    kansen[1][2] = kansen[1][2] * minchance
                    kansen[1][3] = kansen[1][3] * minchance
                    kansen[1][4] = kansen[1][4] * minchance
                    kansen[1][5] = kansen[1][5] * minchance

        kanslist.append([
            kansen[0][0] / kansen[1][0],
            kansen[0][1] / kansen[1][1],
            kansen[0][2] / kansen[1][2],
            kansen[0][3] / kansen[1][3],
            kansen[0][4] / kansen[1][4],
            kansen[0][5] / kansen[1][5]
        ])
    elif len(woord) == 3:
        minchance = 0.1 / trigrammen[0]
        # zoek het trigram in de grote lijst
        encountered = False
        for counter in range(1, len(trigrammen)):
            if trigrammen[counter][0] == woord:
                encountered = True
                kanslist.append([
                    trigrammen[counter][1],
                    trigrammen[counter][2],
                    trigrammen[counter][3],
                    trigrammen[counter][4],
                    trigrammen[counter][5],
                    trigrammen[counter][6],
                ])

        if not encountered:
            minchance = 0.1 / trigrammen[0]
            trigrammen[0] += 0.6
            trigrammen.append(
                [woord, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, minchance, minchance, minchance, minchance, minchance,
                 minchance])
            kanslist.append([
                minchance,
                minchance,
                minchance,
                minchance,
                minchance,
                minchance
            ])
    elif len(woord) == 2:
        minchance = 0.1 / bigrammen[0]
        # zoek het bigram in de grote lijst
        encountered = False
        for counter in range(1, len(bigrammen)):
            if bigrammen[counter][0] == woord:
                encountered = True
                kanslist.append([
                    bigrammen[counter][1],
                    bigrammen[counter][2],
                    bigrammen[counter][3],
                    bigrammen[counter][4],
                    bigrammen[counter][5],
                    bigrammen[counter][6],
                ])

        if not encountered:
            bigrammen[0] += 0.6
            minchance = 0.1 / bigrammen[0]
            bigrammen.append(
                [woord, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, minchance, minchance, minchance, minchance, minchance,
                 minchance])
            kanslist.append([
                minchance,
                minchance,
                minchance,
                minchance,
                minchance,
                minchance
            ])


# Stap 3: de hoogste kans is de taal dat het is.
eindkans = []

# alle kansen van de woorden met elkaar vermenigvuldigen
for kans in range(len(kanslist)):
    if kans == 0:
        eindkans = [
            kanslist[0]
        ]
    else:
        eindkans[0][0] = eindkans[0][0] * kanslist[kans][0]
        eindkans[0][1] = eindkans[0][1] * kanslist[kans][1]
        eindkans[0][2] = eindkans[0][2] * kanslist[kans][2]
        eindkans[0][3] = eindkans[0][3] * kanslist[kans][3]
        eindkans[0][4] = eindkans[0][4] * kanslist[kans][4]
        eindkans[0][5] = eindkans[0][5] * kanslist[kans][5]

# de hoogste kans uit de lijst halen en die als antwoord nemen
ikhebergenseennestteveelgemaaktenikweetnietwaar = eindkans[0]
maxvalue = max(ikhebergenseennestteveelgemaaktenikweetnietwaar)
maxindex = ikhebergenseennestteveelgemaaktenikweetnietwaar.index(maxvalue)
print(str(maxindex))

print("Kansen:")
print("Duits: " + str(eindkans[0][0]))
print("Frans: " + str(eindkans[0][1]))
print("Nederlands: " + str(eindkans[0][2]))
print("Fins: " + str(eindkans[0][3]))
print("Spaans: " + str(eindkans[0][4]))
print("Engels: " + str(eindkans[0][5]))

if maxindex == 0:
    print("Je hebt in het Duits geschreven!")
elif maxindex == 1:
    print("Je hebt in het Frans geschreven!")
elif maxindex == 2:
    print("Je hebt in het Nederlands geschreven!")
elif maxindex == 3:
    print("Je hebt in het Fins geschreven!")
elif maxindex == 4:
    print("Je hebt in het Spaans geschreven!")
else:
    print("Je hebt in het Engels geschreven!")
