"""
Méthodes append() et extend() dans une liste

Éditeur : Laurent REYNAUD
Date : 25-07-2020
"""

personnages = []
prem = [2, 3, 5, 7, 11]

""" 
Utilité de la méthode append() 
La méthode append() permet de rajouter un composant dans une liste 
"""

nouveau = input("Personnage : ")  # Exemple de saisi : le roi

personnages.append(nouveau)  # Ajout de la saisie effectuée dans la liste 'personnages'
print(personnages)  # "['le roi']"

nouveau = input("Personnage : ")  # Exemple d'une nouvelle saisie : le buveur

personnages.append(nouveau)  # Ajout de la saisie effectuée dans la liste 'personnages'
print(personnages)  # "['le roi', 'le buveur']"

""" 
Utilité de la méthode extend() 
La méthode extend() permet de rajouter plusieurs composants dans une liste en une seule fois 
"""

prem.extend([13, 17, 19])  # rajout de ces 3 composants à la liste 'prem'
print(prem)  # "[2, 3, 5, 7, 11, 13, 17, 19]"
