"""
Séquences d'objets non simples (sous-séquences présentes dans des séquences

Éditeur : Laurent REYNAUD
Date : 26-07-2020
"""

personnages = ["le serpent", "le mouton", "le petit prince", "l'aviateur", "la rose", "le Monsieur cramoisi", "le roi",
               "le vaniteux", "le buveur", "le businessman", "l'allumeur de réverbères", "le géographe",
               "la fleur à trois pétales", "les roses du jardin", "le renard", "l'aiguilleur", "le marchand"]

print(personnages)

print(len(personnages))  # 17 composants

print(personnages[0])  # affichage du composant n° 0 : le serpent

print(personnages[0][1])  # affichage du caractère n° 1 du composant n° 0 : e

for elements in personnages:  # Pour chaque composant dans la liste personnages...
    for caracteres in elements:  # ...Et pour chaque caractère de chaque composant...
        print(caracteres, end=" ")  # Afficher le caractère terminé d'un espace
    print()  # Après chaque caractère de chaque composant, passer à la ligne suivante

s = [1, 3, 3.14, ("bon", "jour"), [5, 7]]  # dans cette liste on a des entiers, des réels, un tuple et une sous-liste

print(len(s))  # 5 composants

print(len(s[3]))  # Longueur du tuple présent dans la liste 's' qui a 2 composants ("bon", "jour")

print(len(s[3][1]))  # Longueur du composant 1 ("jour") du composant 3 (tuple) de la liste 's' qui est donc de 4

s[4][1] = 666  # La composante 1 (chiffre 7) de la composante 4 (sous-liste) de la classe 's' est remplacée par 666
print(s)  # [1, 3, 3.14, ("bon", "jour"), [5, 666]]
