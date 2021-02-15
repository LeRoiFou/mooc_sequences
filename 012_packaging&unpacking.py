"""
Emballages et déballages

Éditeur : Laurent REYNAUD
Date : 26-07-2020
"""

tp = 2, 3, 5  # Tuple ici sans parenthèse qui est donc considéré comme une instruction d'emballage
print(tp)  # (2, 3, 5)

x, y, z = tp  # À l'inverse on effectue ici une instruction de déballage
print(x)  # 2
print(y)  # 3
print(z)  # 5

x, y = 33, 666
print(x, y)  # 33 666

x, y = y, x  # On effectue ici une permutation
print(x, y)  # 666 33
