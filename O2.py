import random

#findnextstates ook met kruisjes
#winner bug: hij telt de x en o's samen en geeft een false winner

# Opdracht 2
bord = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def findNextStates(bord):
    states = []
    for i in range(0, len(bord)):
        replica = list(bord)

        if replica[i] == 0:
            replica[i] = "o"
            states.append(replica)
    return states


def move(vak, figuur):
    bord[vak - 1] = figuur
    print("Move:")
    printBoard(bord)


def playerTurn():
    zet = int(input("Het is jouw zet! In welk vakje wil je een zet maken?"))
    move(zet, "x")

    win = checkGoalState(bord)
    if win == -1:
        print("Proficiat! U heeft gewonnen!")
    elif win == 0:
        print("Gelijkspel!")
    else:
        AITurn()


def AITurn():
    print("Zet van de AI...")
    next = findNextStates(bord)
    nextvalues = []
    for state in next:
        nextvalues.append(miniMax(state, True))

    print(next)
    print(nextvalues)

    beststate = []
    bestvalue = 0
    for i in range(0, len(nextvalues)):
        if nextvalues[i] == 1:
            beststate = next[i]
            bestvalue = 1
            break

    if bestvalue != 1:
        for value in nextvalues:
            if value == 0:
                beststate = next[value]
                break

    print(beststate)
    zet = 0
    for i in range(0, len(bord)):
        if bord[i] != beststate[i]:
            zet = i + 1

    move(zet, "o")

    win = checkGoalState(bord)
    if win == 1:
        print("Helaas, U heeft verloren.")
    elif win == 0:
        print("Gelijkspel!")
    else:
        playerTurn()


def printBoard(bord):
    print(str(bord[0]) + "  |  " + str(bord[1]) + "  |  " + str(bord[2]))
    print("--------------------------")
    print(str(bord[3]) + "  |  " + str(bord[4]) + "  |  " + str(bord[5]))
    print("--------------------------")
    print(str(bord[6]) + "  |  " + str(bord[7]) + "  |  " + str(bord[8]))


def checkGoalState(bord):
    #controleer of er drie op een rij is gemaakt
    #kruisjes:
    for i in range(1, 4):
        if bord[(i - 1) * 3] and bord[(i - 1) * 3 + 1] and bord[(i - 1) * 3 + 2] == "x" or bord[0 - 1 + i] and bord[3 - 1 + i] and bord[6 - 1 + i] == "x":
            return -1
    #diagonalen
    if bord[0] and bord[4] and bord[8] == "x" or bord[2] and bord[4] and bord[6] == "x":
        return -1

    #cirkels
    for i in range(1, 4):
        if bord[(i - 1) * 3] and bord[(i - 1) * 3 + 1] and bord[(i - 1) * 3 + 2] == "o" or bord[0 - 1 + i] and bord[3 - 1 + i] and bord[6 - 1 + i] == "o":
            return 1
    #diagonalen
    if bord[0] and bord[4] and bord[8] == "x" or bord[2] and bord[4] and bord[6] == "o":
        return 1

    #controleer of er nog zetten zijn, zo niet, is het gelijkspel
    if 0 in bord:
        return 5
    else:
        return 0


def miniMax(bord, maxing):
    if checkGoalState(bord) != 5:
        return checkGoalState(bord)
    else:
        statevalues = []
        states = findNextStates(bord)
        for state in states:
            statevalues.append(miniMax(state, not maxing))
        if maxing:
            best = max(statevalues)
        else:
            best = min(statevalues)
        return best


def start():
    start = random.randint(0, 1)
    printBoard(bord)
    if start == 0:
        playerTurn()
    else:
        AITurn()


start()

