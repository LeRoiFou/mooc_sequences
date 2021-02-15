"""
Identité des objets

Éditeur : Laurent REYNAUD
Date : 25-07-2020
"""

prem = [2, 3]

prem = sec = [2, 3]  # création de deux noms différents pour une même liste
print(id(prem))  # Python donne ici un n° d'identification pour la variable 'prem'
print(id(sec))  # Python donne ici le même n° d'identification pour cette variable 'sec'

trois = [2, 3]  # Déclaration d'une variable 'trois' qui cette fois-ci ne sera pas égale aux deux autres variables
print(id(prem))
print(id(sec))
print(id(trois))  # Cette fois-ci la variable 'trois' aura un n° d'identification différent de 'prem' et 'sec'

print(prem is sec)  # Renvoi 'True'
print(prem is trois)  # Renvoi 'False'
print(prem == sec)  # Renvoi 'True'
print(prem == trois)  # Renvoi 'True' mais 'prem' et 'trois' ne sont pas les mêmes objets que 'sec' et 'prem'
