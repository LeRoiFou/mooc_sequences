"""
Méthodes prédéfinies de manipulation des séquences (str, tuples et listes)

Éditeur : Laurent REYNAUD
Date : 28-07-2020
"""

""" 
Fonctions min(), max() et sum() 
"""

print(min("Bonjour"))  # B : première lettre de l'alphabet du mot "Bonjour"

print(max("Bonjour"))  # u : dernière lettre de l'alphabet du mot "Bonjour"

print(sum([2, 5, 6]))  # 13 : cette méthode ne marche pas pour les str

""" 
in et index() 
"""

prem = [1, 3, 5, 7, 9]
print(7 in prem)  # True : l'entier 7 se trouve dans la liste prem

print(prem.index(7))  # 3 : l'entier 7 se trouve au 3ème élément de la liste prem

x = 7
if x in prem:
    print(prem.index(x))  # 3 : avec la condition if() si la valeur cherchée n'est pas trouvée, il n'y aura pas d'erreur

""" 
Enumerate() et zip 
"""

amis = ["Sébastien", "Pierre", "Ariane", "Thierry"]
couleurs = ["bleu", "rouge", "vert", "jaune"]

for i, a in enumerate(amis):
    print(i + 1, a)
    """ 
    1 Sébastien 
    2 Pierre 
    3 Ariane 
    4 Thierry 
    """

for a, c in zip(amis, couleurs):
    print(a, "aime la couleur", c)
    """ 
    Sébastien aime la couleur bleu 
    Pierre aime la couleur rouge 
    Ariane aime la couleur vert 
    Thierry aime la couleur jaune 
    """
