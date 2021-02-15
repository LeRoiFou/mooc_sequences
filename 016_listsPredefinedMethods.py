"""
Méthodes prédéfinies de manipulation des listes 

Éditeur : Laurent REYNAUD 
Date : 28-07-2020 
"""

prem = [7, 3, 11, 2, 9, 12, 14, 16, 15]

prem.insert(2, 5)  # insertion de l'entier '5' à l'indice 2
print(prem)  # '[7, 3, 5, 11, 2, 9, 12, 14, 16, 15]'

prem.pop(5)  # supprime l'indice 5 de la liste qui est l'entier '9'
print(prem)  # '[7, 3, 5, 11, 2, 12, 14, 16, 15]'

prem.pop()  # supprime le dernier élément par défaut
print(prem)  # '[7, 3, 5, 11, 2, 12, 14, 16]'

prem.remove(14)  # supprime l'entier '14' de la liste
print(prem)  # '[7, 3, 5, 11, 2, 12, 16]'

prem.reverse()  # renverse l'ordre des éléments de la liste
print(prem)  # '[16, 12, 2, 11, 5, 3, 7]'

prem.sort()  # trie par ordre croissant, voire possibilité d'obtenir plus de précisions sur cette méthode
print(prem)  # '[2, 3, 5, 7, 11, 12, 16]'

l = prem.copy()  # copie superficielle de la liste
print(prem)  # '[2, 3, 5, 7, 11, 12, 16]'

l2 = prem[:]  # équivalent à la méthode copy()
print(prem)  # , '[2, 3, 5, 7, 11, 12, 16]'

del prem[5]  # supprime l'élément 5 de la liste soit l'entier '12'
print(prem)  # '[2, 3, 5, 7, 11, 16]'

l = [3, 1, 2]

print(sorted(l))  # '[1, 2, 3]' : la liste avec la fonction sorted() n'est pas modifiée par rapport à la fonction sort()

l.sort()  # trie par ordre croissant
print(l)  # '[1, 2, 3]'

print(prem[1:3])  # [3, 5] : édition de la liste 'prem' de l'élément 3 à l'élément 4 (élément 5 exclu)

prem[1:3] = [666, 777]  # les éléments 1 à 2 sont modifiés
print(prem)  # '[2, 666, 777, 7, 11, 16]'

prem[3:3] = [444, 555]  # insertion de ces deux éléments dans la liste 'prem' à partir de l'élément 3
print(prem)  # '[2, 666, 777, 444, 555, 7, 11, 16]'

prem[0:0] = [111, 222]  # insertion de ces deux éléments dans la liste 'prem' à partir de l'élément 0
print(prem)  # '[111, 222, 2, 666, 777, 444, 555, 7, 11, 16]'

prem[len(prem): len(prem)] = [888, 999]  # insertion de ces deux éléments dans la liste 'prem' à partir du dernier élt
print(prem)  # '[111, 222, 2, 666, 777, 444, 555, 7, 11, 16, 888, 999]'

prem[len(prem): len(prem)] = [0]  # insertion de cet élément à partir du dernier élément de la liste 'prem'
print(prem)  # '[111, 222, 2, 666, 777, 444, 555, 7, 11, 16, 888, 999, 0]'
