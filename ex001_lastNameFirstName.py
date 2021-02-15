"""
Écrire une fonction signature qui reçoit un paramètre identite . Ce paramètre est un couple (tuple de deux
composantes) dont la première composante représente un nom et la seconde un prénom.

Cette fonction doit retourner la chaîne de caractères formée du prénom suivi du nom, séparés par une espace.

Éditeur : Laurent REYNAUD

Date : 22-07-2020
"""


def signature(identite):
    identite = identite[1] + " " + identite[0]
    return identite


nom = input()
prenom = input()
print(signature((nom, prenom)))
