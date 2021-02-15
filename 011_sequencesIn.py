"""
Tranches et test 'in'

Éditeur : Laurent REYNAUD
Date : 26-07-2020
"""

tex = "bonjour"  # séquence sous la forme d'un str
prem = [2, 3, 5, 7, 8, 9, 10, 13, 17]  # séquence sous la forme d'une liste

prem[4:7] = [11, 13]  # slicing : remplacement de 3 composants (chiffre 13 exclu) par 2 de la liste 'prem'
print(prem)  # [2, 3, 5, 7, 11, 13, 13, 17]

""" 
L'instruction 'in' peut s'appliquer quelque soit la séquence (str, tuple, liste) pour un caractère (voir les deux 
premières lignes ci-dessous). Le recours à l'instruction 'in' pour une sous-chaîne de caractère (voir le 3ème exemple 
ci-dessous) ne s'applique que pour les str (donc non applicable pour les tuples et les listes sauf pour les sous-tuples 
et les sous-listes) 
"""
print(7 in prem)  # True
print("o" in tex)  # True
print("jour" in tex)  # True
