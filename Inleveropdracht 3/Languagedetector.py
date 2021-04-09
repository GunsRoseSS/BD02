import json

# laadt de bigrammen en trigrammen in
with open('Bigrammen.txt', 'r') as f:
    bigrammen = json.loads(f.read())

with open('Trigrammen.txt', 'w') as g:
    trigrammen = json.loads(g.read())

# Stap 1: de herkenner haalt uit de zin alle bigrammen en trigrammen
# Stap 2: en vergelijkt deze met de kansen van de talen
# Stap 3: de hoogste kans is de taal dat het is.