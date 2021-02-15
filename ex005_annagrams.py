"""

Une anagramme d’un mot v est un mot w qui comprend les mêmes lettres que le mot initial v, en même quantité,
mais non nécessairement dans le même ordre (par exemple, « marion » et « romina » sont des anagrammes). Notez que
anagramme est un mot féminin.

Écrire une fonction anagrammes(v, w) qui renvoie la valeur booléenne True si les mots v et w sont des anagrammes.

La fonction retourne la valeur booléenne False dans le cas contraire.
"""


def anagrammes(v, w):
    liste1 = list(v.strip())
    liste2 = list(w.strip())
    liste1.sort()
    liste2.sort()
    if liste1[:] == liste2[:]:
        res = True
    else:
        res = False
    return res


phrase1 = input()
phrase2 = input()
print(anagrammes(phrase1, phrase2))
