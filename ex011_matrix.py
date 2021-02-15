"""
Écrire une fonction init_mat(m, n) qui construit et renvoie une matrice d’entiers initialisée à la matrice nulle et
de dimension m x n.

Exemple 1
L’appel suivant de la fonction :
init_mat(2, 3)
doit retourner :
[[0, 0, 0], [0, 0, 0]]

Exemple 2
L’appel suivant de la fonction :
init_mat(0, 0)
doit retourner :
[]

Éditeur : Laurent REYNAUD
Date : 10-08-2020
"""


def init_mat(m, n):
    liste = [[0] * n for i in range(m)]
    return liste


print("Taille du tableau à l'horizontal :")
horizontal = int(input())
print("Taille du tableau à la verticale :")
vertical = int(input())
print(init_mat(horizontal, vertical))
