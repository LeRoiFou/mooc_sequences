"""
Passage de paramètre de type liste : gestion de la mémoire des séquences sur Python

Éditeur : Laurent REYNAUD
Date : 25-07-2020
"""


def fun(s):
    s[1] = 666  # Variable locale 's[1] : le composant 1 de la liste aura cette valeur


ma_liste = [1, 2, 3]
fun(ma_liste)  # Le composant 1 de la liste 'ma_liste' aura une valeur qui passera de '2' à '666'
print(ma_liste)  # [1, 666, 3]


def funbis(s):
    s = [4, 5, 6]  # Cette variable locale va disparaître dès que cette fonction sera appelée...


funbis(ma_liste)
print(ma_liste)  # [1, 666, 3] -> la variable locale de la fonction funbis() ne s'affice pas ici...
