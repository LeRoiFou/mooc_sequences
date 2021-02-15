"""
Manipulation des listes et des tuples

Éditeur : Laurent REYNAUD
Date : 22-07-2020
"""

asteroide = [325, 326, 327, 328, 329, 330]
personnages = ["le serpent", "le mouton", "le petit prince", "l'aviateur", "la rose", "le Monsieur cramoisi", "le roi",
               "le vaniteux", "le buveur", "le businessman", "l'allumeur de réverbères", "le géographe",
               "la fleur à trois pétales", "les roses du jardin", "le renard", "l'aiguilleur", "le marchand"]
planetes = ["B 612", 325, 326, 327, 328, 329, 330]

# Calcul d'une somme de 1 à 10 : 1 + 2 + 3 +...+ 10
somme = 0
for i in range(10):
    somme += i
print(somme)

# Affichage des composants d'une liste avec la boucle 'for'
for elements in personnages:
    print(elements)

# Autre exemple d'affichage avec la boucle 'for' et 'in'
nom = "Gerald"
for caracteres in nom:
    print("Caractère suivant", caracteres)

# Avec cette instruction dans la boucle 'for' et 'in', on peut afficher pour chaque caractère sa position
for i in range(len(nom)):
    print("Caractère d'indice", i, ":", nom[i])

# Dans l'exemple ci-après, avec l'opérateur 'in', le programme va vérifier si le personnage désigné figure dans la
# liste 'personnages'
personnage = input("Un personnage : ")  # Exemple de saisie : "le roi"
if personnage in personnages:
    print("Il s'agit d'un personnage de la liste \"personnages\"")

# Autres fonctionnalités avec l'opérateur 'in'
prem = [2, 3, 5, 7, 11, 13]
print(7 in prem)  # True
print(9 in prem)  # False

ma_liste = [9, 18, 3, 5, 7, 21]
ma_liste2 = [9, 18, [3, 5, 7], 21]
print([3, 5, 7] in ma_liste)  # False
print([3, 5, 7] in ma_liste2)  # True

print("roi" in personnage)  # True si on a saisi "le roi" dans l'instruction en début du programme
