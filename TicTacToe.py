import random

#findnextstates ook met kruisjes

# Opdracht 2
# print het bord, er wordt van links naar rechts en van boven naar onderen gewerkt
bord = [0, 0, 0, 0, 0, 0, 0, 0, 0]


#vind alle mogelijke states/zetten
def findNextStates(bord, maxing):
    states = [] #een lijst voor alle gevonden states
    #for iedere plek in de lijst
    for i in range(0, len(bord)):
        replica = list(bord) #maak een replica van het bord aan

        if replica[i] == 0: #als er een lege plek is
            if maxing: #en je de maximaliserende speler (in dit geval de cirkel) bent
                replica[i] = "o" #dan vervang de lege plek met een cirkel.
            else: #en je de minimaliserende speler (in dit geval het kruisje) bent
                replica[i] = "x" #dan vervang de lege plek met een kruisje.
        #hierdoor creëer je een nieuwe state.
            states.append(replica) #voeg vervolgens de nieuw gevonden state toe aan de lijst met states.
    return states


#maak een zet
def move(vak, figuur):
    bord[vak - 1] = figuur #vervang de lege plek met het gegeven figuur
    print("Move:")
    printBoard(bord) #print het nieuwe bord.


#controleer of de zet legaal is
def checkIllegalMove(vak):
    if bord[vak - 1] == 0: #if het vakje leeg is
        return True
    else:
        return False

#de beurt van de speler
def playerTurn():
    zet = int(input("Het is jouw zet! In welk vakje wil je een zet maken?")) #vraag de positie van de zet op
    if checkIllegalMove(zet): #controleer of de zet legaal is
        move(zet, "x")  # maak de zet

        win = checkGoalState(bord) #controleer of iemand gewonnen heeft, zo ja, print een statement.
        if win == -1:
            print("Proficiat! U heeft gewonnen!")
        elif win == 0:
            print("Gelijkspel!")
        else:
            AITurn() #zo niet, is de AI aan de beurt.
    else: #als de zet niet legaal is, print een statement en start de beurt overnieuw
        print("Dit vakje is al bezet.")
        playerTurn()


#de beurt van de AI
def AITurn():
    print("Zet van de AI...")
    next = findNextStates(bord, True) #zoek naar de nieuwe states die behaald kunnen worden vanuit de huidige state
    nextvalues = [] #een lijst voor de waarden van de nieuwe states.
    for state in next: #voor iedere state
        nextvalues.append(miniMax(state, True)) #bereken de waarde van deze state met het minimax algoritme en voeg deze toe aan de lijst van waarden.

    beststate = [] #de best mogelijke state
    bestvalue = 0 #de best mogelijke value
    for i in range(0, len(nextvalues)): #voor iedere value van de nieuwe states
        if nextvalues[i] == 1: #als deze winnend is voor de AI
            beststate = next[i] #dan maak deze de beste state en de beste value.
            bestvalue = 1
            break

    if bestvalue != 1: #als er geen winnende state gevonden is
        for i in range(0, len(nextvalues)): #zoek dan naar een state waar er gelijkspel te vinden is.
            if i == 0:
                beststate = next[i]
                break

    zet = 0 #de zet die de AI gaat maken
    for i in range(0, len(bord)): #kijk waar het verschil zit tussen de huidige state en de beste state en gebruik dit verschil als zet.
        if bord[i] != beststate[i]:
            zet = i + 1

    move(zet, "o") #maak de zet.

    win = checkGoalState(bord) #controleer of de Ai gewonnen heeft of gelijk heeft gespeeld.
    if win == 1:
        print("Helaas, U heeft verloren.")
    elif win == 0:
        print("Gelijkspel!")
    else:
        playerTurn() #zo niet, dan is het de beurt van de speler.


#print het bord.
def printBoard(bord):
    placeholder = list(bord) #maak een placeholder zodat het echte bord niet wordt aangepast.
    for i in range(0, len(placeholder)): #maak van de 0 een leeg vakje voor betere leesbaarheid.
        if placeholder[i] == 0:
            placeholder[i] = " "
        else:
            placeholder[i] = str(placeholder[i]) #en maak van de integer een string.

    print(placeholder[0] + "  |  " + placeholder[1] + "  |  " + placeholder[2])
    print("-----------------")
    print(placeholder[3] + "  |  " + placeholder[4] + "  |  " + placeholder[5])
    print("-----------------")
    print(placeholder[6] + "  |  " + placeholder[7] + "  |  " + placeholder[8])


#controleer of het spel voorbij is
def checkGoalState(bord):
    #kruisjes:
    for i in range(1, 4):
        if (bord[(i - 1) * 3] == "x" and bord[(i - 1) * 3 + 1] == "x" and bord[(i - 1) * 3 + 2] == "x") or (bord[0 - 1 + i] == "x" and bord[3 - 1 + i] == "x" and bord[6 - 1 + i] == "x"):
            return -1
    #diagonalen
    if (bord[0] == "x" and bord[4] == "x" and bord[8] == "x") or (bord[2] == "x" and bord[4] == "x" and bord[6] == "x"):
        return -1

    #cirkels
    for i in range(1, 4):
        if (bord[(i - 1) * 3] == "o" and bord[(i - 1) * 3 + 1] == "o" and bord[(i - 1) * 3 + 2] == "o") or (bord[0 - 1 + i] == "o" and bord[3 - 1 + i] == "o" and bord[6 - 1 + i] == "o"):
            return 1
    #diagonalen
    if (bord[0] == "o" and bord[4] == "o" and bord[8] == "o") or (bord[2] == "o" and bord[4] == "o" and bord[6] == "o"):
        return 1

    #controleer of er nog zetten zijn, zo niet, is het gelijkspel
    if 0 in bord:
        return 5
    else:
        return 0


#het minimax algoritme
def miniMax(bord, maxing):
    if checkGoalState(bord) != 5: #als de huidige state een goal state is, return de value van de goalstate
        return checkGoalState(bord)
    else:
        statevalues = [] #de values van de nieuwe states
        states = findNextStates(bord, maxing) #zoek de nieuwe states
        for state in states: #voor iedere gevonden state
            statevalues.append(miniMax(state, not maxing)) #zoek de value van de state dmv de volgende states te zoeken totdat deze tegen een goal state op lopen.

        if maxing: #als het de beurt van de maximaliserende speler is (en de vorige beurt dus van de minimaliserende speler is)
            best = min(statevalues) #geef dan de laagste waarde van alle state values (omdat dit het beste is voor de minimaliserende speler)
        else: #en doe dit andersom als het de beurt van de minimaliserende speler is.
            best = max(statevalues)

        return best #en return deze value


#de start functie
def start():
    start = random.randint(0, 1) #bepaal wie er gaat starten
    printBoard(bord)
    if start == 0:
        playerTurn()
    else:
        AITurn()


start()

