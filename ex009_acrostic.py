"""
D’après Wikipedia, un acrostiche est un poème, une strophe ou une série de strophes fondé sur une forme poétique
consistant en ce que, lues verticalement de haut en bas, la première lettre ou, parfois, les premiers mots d’une
suite de vers composent un mot ou une expression en lien avec le poème.

Écrire une fonction acrostiche qui reçoit en paramètre le nom d’un fichier et qui retourne la chaîne de caractères
formée par les premières lettres de chaque ligne du fichier.

Éditeur : Laurent REYNAUD
Date : 02-08-2020
"""


def acrostiche(fichier, encoding="utf-8"):
    cumul = []
    with open(fichier) as fichier:
        for line in fichier:
            cumul += line[0]
            res = "".join(cumul)
    return res


print(acrostiche("pieces/accro1.txt"))
