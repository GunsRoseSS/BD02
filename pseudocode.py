# 1A
#
# Dit programma zal de gebruiker toestaan een list van cijfers te sorteren op een decrease and conquer manier.
#
# functie DecreaseAndConquer(lijst, sublijst)
#     if de lijst leeg is,
# 		return de sublijst
#
#     else
#         gooi een cijfer van de lijst in de sublijst(en verwijder deze dus uit de lijst)
#         en sorteer de sublijst:
#
#         neem het cijfer dat net in de sublijst gezet is (a)
#         en neem het cijfer dat voor het cijfer in de lijst staat.(b)
#
#         while het cijfer b groter is dan het cijfer a:
#           verwissel de cijfers,
#           en maak het cijfer dat nu voor het cijfer a in de lijst staat het nieuwe cijfer b.
#
#         return DecreaseAndConquer(lijst, sublijst)
#         en herhaal het proces totdat alle cijfers uit de lijst zijn gehaald.


# 1B
#
# Dit programma zal de gebruiker toestaan een list van cijfers te sorteren op een divide and conquer manier.
#
# functie DivideAndConquer(lijst)
#     if de lengte van de lijst kleiner dan 2 is,
#         return de lijst
#
#     else
#         Splits de lijst in twee sublijsten. (A en B)
#
#         splits en sorteer deze sublijsten met:
#         A = DivideAndConquer(A)
#         B = DivideAndConquer(B)
#
#         maak een nieuwe lijst aan. (C)
#         merge deze lijsten nu met:
#
#         while de lengte van A > 0 and de lengte van B > 0
#             if het eerste cijfer van A > het eerste cijfer van B
#                 zet getal B in lijst C
#                 en verwijder deze uit B.
#             else
#                 zet getal A in lijst C
#                 en verwijder deze uit A.
#
#         nu een van de lijsten leeg is:
#
#         if A is leeg
#             gooi de rest van A in C
#         else
#             gooi de rest van B in C
#
#         C is nu de nieuwe gesorteerde en gemergede lijst.
#         return C

# 2
#
# Dit programma zal de gebruiker toestaan een string van letters om te draaien
#
# functie Omdraaien(string)
#     if de lengte van de string kleiner dan 2 is,
#         return de string
#
#     else
#         neem de eerste letter van de string (e)
#         en verwijder deze uit de string.

#         neem de laatste letter van de string (l)
#         en verwijder deze uit de string.
#
#         return l + Omdraaien(string) + e

# 3
#
# Dit programma zal de gebruiker toestaan om een aantal gewichten uit een lijst te balanceren op een weegschaal.
#
# functie Balanceren(lijst, linkerschaal, rechterschaal)
#     if de lijst leeg is,
#         return beide weegschalen
#
#     else
#         neem het zwaarste gewicht uit de lijst (a)
#
#         if de linker weegschaal zwaarder is dan de rechter
#             voeg het gewicht toe aan de rechter weegschaal
#
#         else
#             voeg het gewicht toe aan de linker weegschaal
#
#         return Balanceren(lijst, linkerschaal, rechterschaal)
#         en ga door totdat er geen gewichten meer over zijn.

# 4

# functie Hanoi(aantal schijven, eerste pin, tweede pin, derde pin)
#     als het aantal schijven een is,
#         verplaats de schijf van de een van de pinnen naar een andere pin
#         geef alle drie de pinnen terug
    
#     Hanoi(aantal schijven min een, eerste pin, derde pin, tweede pin)
#     verplaats de schijf van de een van de pinnen naar een andere pin

#     geef terug Hanoi(aantal schijven min een, tweede pin, eerste pin, derde pin)
#     ga door todat alle schijven zijn gesorteerd
