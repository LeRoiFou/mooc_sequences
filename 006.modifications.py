"""
Listes modifiables // Tuples et str (chaînes de caractères) non modifiables

Éditeur : Laurent REYNAUD
Date : 25-07-2020
"""

""" 
Exemple d'une liste modifiable : 
"""

prem = [2, 3, 5, 7, 9]  # liste

prem[4] = 11  # Changement de la valeur de la dernière composante qui ne peut pas être effectuée avec un tuple / str
print(prem)  # "[2, 3, 5, 7, 11]"

""" 
Exemple d'un str (chaîne de caractères) non modifiable : 
Avec le str ci-après, si on modifie le 1er caractère 'B' par 'C' en procédant de la même manière qu'une liste comme 
ci-avant, à savoir text[0] = "C", un message d'erreur sera affiché 
"""

text = "Bonjour"  # str

text = "C" + text[1:]  # Pour changer un caractère d'un str, il faut réaffecter cette variable avec une nouvelle str
print(text)  # "Conjour"

""" 
Exemple d'un tuple non modifiable : 
Avec le tuple ci-après, si on modifier le 2ème composant du tuple '3' par 0 en procédant de la même manière qu'une liste 
comme ci-avant, à savoir mon_tup[1] = 0, un message d'erreur sera affiché comme pour le str 
"""

mon_tup = (3.14, 3, 66)  # tuple
