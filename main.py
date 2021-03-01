# pseudocode BD02 Richard en Bas
#
# Opdracht 1: sorteer een lijst dmv decrease and conquer
unsortedlist = []

#Opdracht 1A decrease and conquer
def InsertionSort(A, i):
    current = A[i] #selecteert het huidige nummer dat vergeleken wordt met nummers in de lijst
    j = i - 1
    while j >= 0 and A[j] > current: #vergelijk current met het nummer dat voor current in de lijst staat, en wissel deze om waar nodig.
        A[j + 1] = A[j]
        j -= 1
        A[j + 1] = current
    return A


B = [] #de sublijst die gesorteerd wordt


def dsort(A, B):
    if len(A) == 0: #als er geen nummers meer zijn die gesorteerd worden, dan return de gesorteerde lijst
        return B
    else:
        B.append(A[0]) #voeg een nummer toe aan de sublijst
        A.pop(0) #verwijder het nummer uit de originele lijst
        B = InsertionSort(B, len(B) - 1) #voer de insertionsort iteratie uit
        return dsort(A, B)


# print(dsort([88, 6, 4, 72, 1], B)) #voorbeeld uitwerking

#Opdracht 1B divide and conquer
def QuickSort(A):
    if len(A) <= 1: #als de lengte van de lijst kleiner dan 1 is, return dan de lijst
        return A
    else:
        pivot = A.pop() #verwijder het laatste nummer uit de lijst en maak deze de pivot

        list_higher = [] #maakt de lijsten aan
        list_lower = []

        for number in A:
            if number > pivot: #als het nummer hoger is dan de pivot, zet deze in de hogere lijst
                list_higher.append(number)
            else: #zo niet, zet ze in de lagere lijst (inclusief nummers die gelijk zijn)
                list_lower.append(number)
        return QuickSort(list_lower) + [pivot] + QuickSort(list_higher)

#print(QuickSort([85,25,84,15,26,37,95,0,34])) #voorbeeld uitwerking

#Opdracht 2 string van s letters omdraaien
def LetterSort(s):
    if len(s) <= 1: #Als de string kleiner dan 2 letters is, dan return de string
        return s
    else:
        first = s[:1] #de eerste letter, die naar achteren moet
        last = s[len(s)-1:] #de laaste letter, die naar voren moet
        leftover = s[1:len(s)-1] #de rest van de string
        return last + LetterSort(leftover) + first

#print(LetterSort("Markisacunt")) #voorbeeld uitwerking

#Opdracht 3