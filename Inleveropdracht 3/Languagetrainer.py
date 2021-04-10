import json

# stap 1: haal alle documenten op en format deze
doc = open('DE.txt', 'r', encoding='utf-8')  # encoding zorgt ervoor dat de speciale karakters gelezen worden
DE = doc.read().replace("\n", " ")  # duits
doc.close()

doc = open('FR.txt', 'r', encoding='utf-8')
FR = doc.read().replace("\n", " ")  # frans
doc.close()

doc = open('NL.txt', 'r', encoding='utf-8')
NL = doc.read().replace("\n", " ")  # engels
doc.close()

doc = open('FI.txt', 'r', encoding='utf-8')
FI = doc.read().replace("\n", " ")  # fins
doc.close()

doc = open('ES.txt', 'r', encoding='utf-8')
ES = doc.read().replace("\n", " ")  # spaans
doc.close()

doc = open('EN.txt', 'r', encoding='utf-8')
EN = doc.read().replace("\n", " ")  # engels
doc.close()

# stap 2: haal uit ieder document alle bi en trigrammen en zet deze in een (turf)tabel
# alle letters/tekens die we in een trigram willen zetten
charlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "ä", "Ä", "à", "À", "á", "Á", "â", "Â", "å", "Å", "ã", "Ã", "æ", "Æ", "Ç", "ü", "é", "ç", "ê", "ë", "è", "ï", "î", "ì", "ô", "ö", "ò", "û", "ù", "ÿ", "¢", "í", "ó", "ú", "ñ", "Ñ", "ß", "µ", "Š", "š", "œ", "Ÿ", "È", "É", "Ê", "Ë", "Ì", "Í", "Î", "Ï", "Ð", "Ò", "Ó", "Ô", "Õ", "Ö", "Ø", "Ù", "Ú", "Û", "Ü", "Ý", "õ", "ø", "ü", "ý"]
langlist = [DE, FR, NL, FI, ES, EN] #de talen
trigramlist = [0] #de 0 is het totaal aantal trigrammen
bigramlist = [0] #idem

for language in langlist:
    for letter in range(len(language) - 2):  # -2, omdat je in de laatste 2 letters geen trigram meer kan maken
        trigram = language[letter:letter + 3]
        bigram = language[letter:letter + 2]

        #trigram toevoeger
        if trigram[0] in charlist and trigram[1] in charlist and trigram[2] in charlist: #als de trigram valide is (geen spaties of rare karakters)
            existing = False
            for checker in range(len(trigramlist)):
                if checker != 0 and trigramlist[checker][0] == trigram: #als de trigram al in de lijst staat
                    trigramlist[checker][langlist.index(language) + 1] += 1 #dan voeg een entry toe aan de taal
                    existing = True
                    trigramlist[0] += 1
                    break

            if not existing: #als deze niet in de lijst is voorgekomen
                newtrigram = [trigram, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
                newtrigram[langlist.index(language) + 1] += 1
                trigramlist.append(newtrigram)
                trigramlist[0] += 1.6

        # bigram toevoeger
        if bigram[0] in charlist and bigram[1] in charlist: #als de bigram valide is (geen spaties of rare karakters)
            existing = False
            for checker in range(len(bigramlist)):
                if checker != 0 and bigramlist[checker][0] == bigram: #als de bigram al in de lijst staat
                    bigramlist[checker][langlist.index(language) + 1] += 1 #dan voeg een entry toe aan de taal
                    existing = True
                    bigramlist[0] += 1
                    break

            if not existing: #als deze niet in de lijst is voorgekomen
                newbigram = [bigram, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
                newbigram[langlist.index(language) + 1] += 1
                bigramlist.append(newbigram)
                bigramlist[0] += 1.6

# stap 3: maak van de turftabel een tabel met kansen
for trigram in range(len(trigramlist)):
    if trigram != 0:
        # bereken alle kansen en voeg deze toe in het rijtje
        trigramlist[trigram].append(trigramlist[trigram][1] / trigramlist[0])
        trigramlist[trigram].append(trigramlist[trigram][2] / trigramlist[0])
        trigramlist[trigram].append(trigramlist[trigram][3] / trigramlist[0])
        trigramlist[trigram].append(trigramlist[trigram][4] / trigramlist[0])
        trigramlist[trigram].append(trigramlist[trigram][5] / trigramlist[0])
        trigramlist[trigram].append(trigramlist[trigram][6] / trigramlist[0])

for bigram in range(len(bigramlist)):
    if bigram != 0:
        # bereken alle kansen en voeg deze toe in het rijtje
        bigramlist[bigram].append(bigramlist[bigram][1] / bigramlist[0])
        bigramlist[bigram].append(bigramlist[bigram][2] / bigramlist[0])
        bigramlist[bigram].append(bigramlist[bigram][3] / bigramlist[0])
        bigramlist[bigram].append(bigramlist[bigram][4] / bigramlist[0])
        bigramlist[bigram].append(bigramlist[bigram][5] / bigramlist[0])
        bigramlist[bigram].append(bigramlist[bigram][6] / bigramlist[0])

# stap 4: sla deze tabel ergens permanent op
# source: https://www.codegrepper.com/code-examples/python/python+save+list+to+file+txt
with open('Bigrammen.txt', 'w') as f:
    f.write(json.dumps(bigramlist))

with open('Trigrammen.txt', 'w') as g:
    g.write((json.dumps(trigramlist)))

