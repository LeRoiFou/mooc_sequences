"""
Concepts de compréhension et copie profonde de liste 
Éditeur : Laurent REYNAUD 
Date : 29-07-2020 
"""
""" 
Concept de compréhension de liste 
"""
squares = [x ** 2 for x in range(10)]  # ce qui équivaut à [0², 1², 2², 3²..., 9²]
print(squares)  # '[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]'
m = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]  # couples avec des valeurs différentes de x et y
print(m)  # '[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]'
m2 = []  # autre instruction permettant également d'obtenir une liste de couples avec les valeurs différentes de x et y
for x in range(1, 4):
    for y in range(1, 4):
        if x != y:
            m2.append((x, y))
print(m2)  # '[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]'
""" 
Copie superficielle de liste (shallow copy) 
"""
s = [2, 3, 5, 7]
t = s[:]  # copie de la liste 's'
print(s)  # '[2, 3, 5, 7]'
print(t)  # '[2, 3, 5, 7]'
s = [2, 3, [5, 7]]
t = s[:]
print(s)  # '[2, 3, [5, 7]]'
print(t)  # '[2, 3, [5, 7]]'
s[0] = 999
s[2][0] = 666
print(s)  # '[999, 3, [666, 7]]'
print(t)  # '[2, 3, [666, 7]]' : la sous-liste initialement '[5, 7] est UNIQUE par rapport à la liste de base !!!
""" 
La copie d'une sous-liste montre les limites d'une copie superficielle, il faut donc recourir à une copie profonde... 
"""
""" 
Copie profonde d'une liste (deep copy) 
"""
from copy import deepcopy

s = [2, 3, [5, 7]]
t = deepcopy(s)
s[2][0] = 666
print(s)  # '[2, 3, [666, 7]]'
print(t)  # '[2, 3, [5, 7]]'
""" 
Avec une copie profonde, la modification d'une sous-liste dans une liste initiale ne s'impacte pas dans la liste copiée, 
car avec la fonction prédéfinie deepcopy(), il n'y a pas de sous-liste commune entre la liste initiale et la liste 
copiée 
"""
