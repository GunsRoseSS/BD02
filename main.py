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

#print(LetterSort("zuydhogeschool")) #voorbeeld uitwerking

#Opdracht 3 Weegschaal
balance1 = 0
balance2 = 0
def WeightSort(A, balance1, balance2):
    if len(A) == 0:
        return "Weegschaal 1: " + str(balance1) + " Weegschaal 2: " + str(balance2)
    else:
        A.sort()
        selectedweight = A.pop()
        if balance1 < balance2:
            balance1 += selectedweight
        else:
            balance2 += selectedweight
        return WeightSort(A, balance1, balance2)

# print(WeightSort([1,5,6,7,3,2,6,6,3,2], balance1, balance2)) #voorbeeld uitwerking

# Opdracht 4 Torens van Hanoi
# Hulp gehad van https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
# En http://pythontutor.com/visualize.html#mode=edit
def Hanoi(disks, start, aid, destination):
    if disks == 1:
        print(start[0], "pin:", start[1], aid[0], "pin:", aid[1],
              destination[0], "pin:", destination[1])
        destination[1].append(start[1].pop())
        print(start[0], "pin:", start[1], aid[0], "pin:", aid[1],
              destination[0], "pin:", destination[1])
        return start, aid, destination

    Hanoi(disks - 1, start, destination, aid)

    destination[1].append(start[1].pop())
    print(start[0], "pin:", start[1], aid[0], "pin:", aid[1],
          destination[0], "pin:", destination[1])

    return Hanoi(disks - 1, aid, start, destination)


# Configuratie,
# Disks is het aantal schijven op de start paal
# de lijsten: start, aid en destination representateren de drie palen
# In de lijsten representateert het meest rechtse getal de onderste schijf en
# het meest linkse getal de bovenste schijf.
# Dus van rechts naar links in de lijst is van onder naar boven op de pilaren.
disks = 5
start = ["Start", []]
aid = ["Aid", []]
destination = ["Destination", []]
for i in range(disks, 0, -1):
    start[1].append(i)
start, aid, destination = Hanoi(disks, start, aid, destination)
print("End result:", start[0], "pin:", start[1], aid[0], "pin:",
      aid[1], destination[0], "pin:", destination[1])
