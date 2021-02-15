"""
Les listes et les tuples :

Éditeur : Laurent REYNAUD
Date : 22-07-2020
"""

# Création de listes
asteroide = [325, 326, 327, 328, 329, 330]
personnages = ["le serpent", "le mouton", "le petit prince", "l'aviateur", "la rose", "le Monsieur cramoisi", "le roi",
               "le vaniteux", "le buveur", "le businessman", "l'allumeur de réverbères", "le géographe",
               "la fleur à trois pétales", "les roses du jardin", "le renard", "l'aiguilleur", "le marchand"]
planetes = ["B 612", 325, 326, 327, 328, 329, 330]
# Cette 3ème liste comprend aussi bien une chaîne de caractères que des entiers (ce qui n'est pas le cas pour Java)
vide = []

# Création de tuples qui sont encadrés par des '()' alors que les listes sont encadrés par des []
mon_tup = (325, 326, 327, 328, 329, 330)
print(mon_tup[0])  # Accès du 1er composant du tuple : '325'
print(len(mon_tup))  # Longueur du tuple : 6
print(type(mon_tup))  # Type de la variable : 'tuple'
