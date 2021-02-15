"""
Combinaison de listes avec les fonctions

Supposons que l’on ait une liste 'mes_valeurs' de valeurs entières
positives correspondant aux vents maximums enregistrés aux Bermudes chaque année depuis l’an 2000, la composante 0
désignant l’an 2000, 1, 2001, ….

La fonction 'categorie()' renvoie la catégorie de cyclone selon la valeur attribuée au vent

La fonction 'historique_tempetes()' doit traiter chaque élément de la liste 'mes_valeurs' séquentiellement.
Pour chaque composant, il faut tester dans quelle catégorie se trouve la valeur :
-> vent < 64 km/h : pas de tempête enregistrée
-> vent >= 64 km/h et < 119 km/h : au moins une tempête mais pas de cyclone
-> vente >= 119 km/h : cyclone avec la catégorie rattachée au regard de la fonction 'catégorie()'

Éditeur : Laurent REYNAUD
Date : 22-07-2020
"""

# Liste des vents maximum enregistrés aux Bermudes depuis l'année 2000
mes_valeurs = [75, 200, 230, 260, 100, 80, 50, 45, 180, 100, 200, 63, 64, 65, 118, 119, 153, 154, 280, 345]
print(len(mes_valeurs))  # résultat = 20 : affichage des valeurs de l'an 2000 à l'an 2019


def categorie(vent):
    """renvoie la catégorie de cyclone enregistré en fonction du vent supérieure à 118 km/h"""

    assert vent > 118  # sinon provoque une erreur dans le code

    if vent < 154:
        res = 1  # catégorie 1
    elif vent < 178:
        res = 2  # catégorie 2
    elif vent < 210:
        res = 3  # catégorie 3
    elif vent < 251:
        res = 4  # catégorie 4
    else:  # catégorie 5
        res = 5
    return res


def historique_tempetes(vent_max):
    """affiche pour chaque année la catégorie de vents subis cette année-là
   entrée : vent_max: liste des vents maximums enregistrés en km/h
   chaque année (composante 0 étant pour l'an 2000)"""

    annee = 2000
    for vent in vent_max:
        if vent < 64:
            print("En", annee, ": pas de tempête enregistrée")
        elif vent < 119:
            print("En", annee, ": il y a eu au moins une tempête mais pas de cyclone")
        else:
            print("En", annee, ": le plus gros cyclone enregistré était de catégorie",
                  categorie(vent))
        annee += 1

historique_tempetes(mes_valeurs)
