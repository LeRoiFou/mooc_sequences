"""
Écrire une fonction my_pow qui prend comme paramètres un nombre entier m et unnombre flottant b, et qui renvoie une
liste contenant les m premières puissances de b, c’est-à-dire une liste contenant les nombres allant de
b^0 à b^{m -1}.
Si le type des paramètres n’est pas celui attendu, la fonction retournera la valeur None.

Exemple 1
L’appel suivant de la fonction :
my_pow(3, 5.0)
doit retourner :
[1.0, 5.0, 25.0]

Exemple 2
L’appel suivant de la fonction :
my_pow(3.0, 5.0)
doit retourner :
None

Exemple 3
L’appel suivant de la fonction :
my_pow('a', 'b')
doit retourner :
None

Éditeur : Laurent REYNAUD
Date : 29-07-2020
"""


def my_pow(m, b):
    # m est un entier int et # b est un réel float
    resultat = 0
    liste = []
    if type(m) == int and type(b) == float:
        for i in range(0, m):
            resultat = b ** i
            liste.append(resultat)
    else:
        liste = None
    return liste


print(my_pow("a", "b"))
