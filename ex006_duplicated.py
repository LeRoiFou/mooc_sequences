"""
Écrire une fonction dupliques qui reçoit une séquence en paramètre.

La fonction doit renvoyer la valeur booléenne True si la séquence passée en paramètre contient des éléments
dupliqués, et la valeur booléenne False sinon.

Exemple 1
L’appel suivant de la fonction :
dupliques([1, 2, 3, 4])
doit retourner :
False

Exemple 2
L’appel suivant de la fonction :
dupliques(['a', 'b', 'c', 'a'])
doit retourner :
True

Exemple 3
L’appel suivant de la fonction :
dupliques('abcda')
doit retourner :
True

Éditeur : Laurent REYNAUD
Date : 28-07-2020
"""


def dupliques(chaine):
    res = ""
    if chaine == "":
        return False
    for c in chaine:
        if chaine.count(c) > 1:
            return True
        else:
            res = False
    return res


print(dupliques([1, 2, 3, 4]))
print(dupliques(['a', 'b', 'c', 'a']))
print(dupliques('abcda'))
print(dupliques(""))
