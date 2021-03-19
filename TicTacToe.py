# Opdracht 2

import random
bord = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# bord = ["x", 0, "o", "o", "x", 0, 0, 0, "o"]


def findNextStates(bord, maxing):
    """Vind alle mogelijke states/zetten voor de kunstmatige intelligentie.

    argumenten:\n
    bord (list) -- een lijst van het speelbord.\n
    maxing (bool) -- of het de minimaliserende (false) of
    maximaliserende (true) speler is.
    """

    # Een lijst voor alle gevonden states.
    states = []
    # Voor iedere plek in de lijst.
    for i in range(0, len(bord)):
        # Maak een replica van het bord aan.
        replica = list(bord)
        # Als er een lege plek is.
        if replica[i] == 0:
            # Als het de maximaliserende speler (in dit geval de cirkel) is.
            if maxing:
                # Vervang de lege plek met een cirkel.
                replica[i] = "o"
            # Als het de minimaliserende speler (in dit geval het kruisje) is.
            else:
                # Vervang de lege plek met een kruisje.
                replica[i] = "x"
            # Creëer een nieuwe state
            # en voeg vervolgens de nieuw gevonden state
            # toe aan de lijst met states.
            states.append(replica)
    return states


def move(vak, figuur):
    """maak een zet.

    argumenten:\n
    vak (int) -- positie waar de speler zijn teken wil neerzetten (1 t/m 9).\n
    figuur (string) -- welk figuur heeft de speler. (x of o)5
    """

    # Vervang de lege plek met het gegeven figuur
    bord[vak - 1] = figuur
    print("Move: ")
    # Print het aangepaste bord.
    printBoard(bord)


def AskUserInput():
    """Vraag en controleer de input van de speler"""

    try:
        zet = int(input("Het is jouw zet! "
                        "In welk vakje wil je een zet maken? "))
    except ValueError:
        print("Er is geen nummer ingevuld, probeer opnieuw")
        zet = AskUserInput()
        return zet
    else:
        if zet in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return zet
        else:
            print("Dit is een incorrect nummer, voer een nummer in "
                  "binnen het bereik van 1 t/m 9")
            zet = AskUserInput()
            return zet


def checkIllegalMove(vak):
    """controleer of de zet wel mag

    vak (int) -- positie waar de speler zijn teken wil neerzetten (1 t/m 9).
    """

    # Als het vakje leeg is
    if bord[vak - 1] == 0:
        return True
    else:
        return False


def playerTurn():
    """Functie om de speler zijn zet te laten zetten"""

    # Vraag de positie van de zet op en controleer of de input correct is.
    zet = AskUserInput()
    # Controleer of de zet wel mag is
    if checkIllegalMove(zet):
        # Maak de zet.
        move(zet, "x")

        # Controleer of iemand gewonnen heeft, zo ja, print een statement.
        win = checkGoalState(bord)
        if win == -1:
            print("Proficiat! U heeft gewonnen!")
        elif win == 0:
            print("Gelijkspel!")
        else:
            # Zo niet, is de AI aan de beurt.
            AITurn()
    # Als de zet niet mag, print een statement en start de beurt overnieuw.
    else:
        print("Dit vakje is al bezet.")
        playerTurn()


def AITurn():
    """Functie om de kunstmatige intelligentie zijn zet te laten zetten"""

    print("Zet van de AI...")
    # Zoek naar de nieuwe states die behaald kunnen worden
    # vanuit de huidige state.
    next = findNextStates(bord, True)
    # Een lijst voor de waarden van de nieuwe states.
    nextvalues = []
    # Voor iedere state.
    for state in next:
        # Bereken de waarde van deze state met het minimax algoritme
        # en voeg deze toe aan de lijst van waarden.
        nextvalues.append(miniMax(state, True, -2, 2))

    # De best mogelijke state.
    beststate = []
    # De best mogelijke value.
    bestvalue = 0

    print(next, nextvalues)
    # Voor iedere value van de nieuwe states.
    for i in range(0, len(nextvalues)):
        # Als deze winnend is voor de AI.
        if nextvalues[i] == 1:
            # Dan maak deze de beste state en de beste value.
            beststate = next[i]
            bestvalue = 1
            break

    # Als er geen winnende state gevonden is.
    if bestvalue != 1:
        # Zoek dan naar een state waar er gelijkspel te vinden is.
        for i in range(0, len(nextvalues)):
            if nextvalues[i] == 0:
                print("h")
                beststate = next[i]
                break

    # De zet die de ki gaat maken.
    zet = 0
    # Kijk waar het verschil zit tussen de huidige state en de beste state
    # en gebruik dit verschil als zet.
    for i in range(0, len(bord)):
        if bord[i] != beststate[i]:
            zet = i + 1
    # Maak de zet.
    move(zet, "o")

    # Controleer of de ki gewonnen heeft of gelijk heeft gespeeld.
    win = checkGoalState(bord)
    if win == 1:
        print("Helaas, U heeft verloren.")
    elif win == 0:
        print("Gelijkspel!")
    else:
        # Zo niet, dan is het de beurt van de speler.
        playerTurn()


def printBoard(bord):
    """print het bord, er wordt van links naar rechts
    en van boven naar onderen gewerkt.

    bord (list) -- een lijst van het speelbord.
    """

    # Maak een placeholder lijst aan zodat het echte bord niet wordt aangepast.
    placeholder = list(bord)
    # Maak van de 0 een leeg vakje voor betere leesbaarheid.
    for i in range(0, len(placeholder)):
        if placeholder[i] == 0:
            placeholder[i] = " "
        else:
            # En maak van de integer een string.
            placeholder[i] = str(placeholder[i])

    print('{:^3}|{:^3}|{:^3}'.format(placeholder[0],
                                     placeholder[1],
                                     placeholder[2]))
    print('{:-^11}'.format('-'))
    print('{:^3}|{:^3}|{:^3}'.format(placeholder[3],
                                     placeholder[4],
                                     placeholder[5]))
    print('{:-^11}'.format('-'))
    print('{:^3}|{:^3}|{:^3}'.format(placeholder[6],
                                     placeholder[7],
                                     placeholder[8]))


def checkGoalState(bord):
    """Functie die controleerd of het spel voorbij is"""

    # Kruisjes:
    for i in range(1, 4):
        if ((bord[(i - 1) * 3] == "x" and
                bord[(i - 1) * 3 + 1] == "x" and
                bord[(i - 1) * 3 + 2] == "x") or
                (bord[0 - 1 + i] == "x" and
                bord[3 - 1 + i] == "x" and
                bord[6 - 1 + i] == "x")):
            return -1

    # Diagonalen:
    if ((bord[0] == "x" and
            bord[4] == "x" and
            bord[8] == "x") or
            (bord[2] == "x" and
            bord[4] == "x" and
            bord[6] == "x")):
        return -1

    # Cirkels:
    for i in range(1, 4):
        if ((bord[(i - 1) * 3] == "o" and
                bord[(i - 1) * 3 + 1] == "o" and
                bord[(i - 1) * 3 + 2] == "o") or
                (bord[0 - 1 + i] == "o" and
                bord[3 - 1 + i] == "o" and
                bord[6 - 1 + i] == "o")):
            return 1

    # Diagonalen:
    if ((bord[0] == "o" and
            bord[4] == "o" and
            bord[8] == "o") or
            (bord[2] == "o" and
            bord[4] == "o" and
            bord[6] == "o")):
        return 1

    # Controleer of er nog zetten zijn, zo niet, is het gelijkspel.
    if 0 in bord:
        return 5
    else:
        return 0


def miniMax(bord, maxing, a, b):
    """het minimax algoritme
    Als de huidige state een goal state is, return de value van de goalstate.
    """

    # Als de huidige state een goal state is, return de value van de goalstate.
    if checkGoalState(bord) != 5:
        return checkGoalState(bord)
    else:
        # De values van de nieuwe states.
        statevalues = []
        # Zoek de nieuwe states.
        states = findNextStates(bord, not maxing)
        # Voor iedere gevonden state.
        for state in states:
            loop = miniMax(state, not maxing, a, b)
            # Zoek de value van de state dmv de volgende states te zoeken
            # totdat deze tegen een goal state op lopen.
            statevalues.append(loop)

            # Als het de beurt van de maximaliserende speler is
            # (en de vorige beurt dus van de minimaliserende speler is).
            if maxing:
                # Kijk dan of de beta verhoogd is.
                b = min(b, loop)
                # En als deze hoger is dan de alpha, break uit de loop
                # (want deze tak wordt nooit gekozen door de speler).
                if b <= a:
                    break
            # En doe dit andersom voor de minimaliserende speler.
            else:
                a = max(a, loop)
                if b <= a:
                    break

        # Als het de beurt van de maximaliserende speler is
        # (en de vorige beurt dus van de minimaliserende speler is).
        if maxing:
            # Geef dan de laagste waarde van alle state values
            # (omdat dit het beste voor de minimaliserende speler is).
            best = min(statevalues)
        # Doe dit andersom als het de beurt van de minimaliserende speler is.
        else:
            best = max(statevalues)
        # En return deze value
        return best


def start():
    """de start functie"""

    # bepaal wie er gaat starten
    start = random.randint(0, 1)
    printBoard(bord)
    if start == 0:
        playerTurn()
    else:
        AITurn()


start()
