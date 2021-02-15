"""
On représente un brin d’ADN par une chaîne de caractères dont les caractères sont parmi les quatre suivants :
'A' (Adénine), 'C' (Cytosine), 'G' (Guanine) et 'T' (Thymine).

Écrire une fonction est_adn qui reçoit une chaîne de caractères en paramètre et qui retourne True si cette chaîne de
caractères n'est pas vide et peut représenter un brin d’ADN, False sinon.

Éditeur : Laurent REYNAUD
Date : 23-07-2020
"""


def est_adn(lettres):
    if lettres == "":
        return False
    for caracteres in lettres:
        if caracteres in "aBbcDdEeFfgHhIiJjKdLlMmNnOoPpQqRrSstUuVvWwXxYyz\" \"":
            return False
    return True


phrase = input()
print(est_adn(phrase))
