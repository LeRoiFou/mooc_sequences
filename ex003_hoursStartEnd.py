"""
Écrire une fonction duree qui reçoit deux paramètres debut et fin. Ces derniers sont des couples (tuples de deux
composantes) dont la première composante représente une heure et la seconde les minutes.

Cette fonction doit calculer la durée qui s’est écoulée entre ces deux instants. Le résultat sera donné sous la forme
d’un tuple (heure, minutes).

Exemple 1:
duree ((14, 39), (18, 45)) doit retourner (4, 6)
Exemple 2:
duree ((6, 0), (5, 15)) doit retourner (23, 15)

Éditeur : Laurent REYNAUD
Date : 23-07-2020
"""


def duree(debut, fin):
    (debut, fin) = (debut[0], debut[1]), (fin[0], fin[1])
    temps_deb = debut[0] * 60 + debut[1]
    temps_fin = fin[0] * 60 + fin[1]
    if temps_fin > temps_deb:
        if temps_fin - temps_deb < 1:
            H = 0
            M = (temps_fin - temps_deb) * 60
        else:
            H = (temps_fin - temps_deb) // 60
            M = int(round((((temps_fin - temps_deb) / 60 - H) * 60), 0))
    else:
        H = (23 - (temps_deb - temps_fin) // 60)
        M = int(round((((24 - (temps_deb - temps_fin) / 60) - H) * 60), 0))
        if M == 60:
            H = (24 - (temps_deb - temps_fin) // 60)
            M = 0
    return H, M


heure_debut = int(input())
minutes_debut = int(input())
heure_fin = int(input())
minutes_fin = int(input())
print(duree((heure_debut, minutes_debut), (heure_fin, minutes_fin)))
