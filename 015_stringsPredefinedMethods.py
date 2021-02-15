"""
Méthodes prédéfinies de manipulation des chaînes de caractères

Éditeur : Laurent REYNAUD
Date : 28-07-2020
"""

s = 'Bonjour'

print(s.lower())  # 'bonjour' : minuscules

print(s.upper())  # 'BONJOUR' : majuscules

print(s.islower())  # 'False' : car la première lettre de 'Bonjour' est en majuscule

print(s.isdigit())  # 'False' : car la variable 's' ne comprend qu'un str

print(s.isalnum())  # 'True' : car la variable 's' ne contient que des caractères alphanumériques

print(s.isalpha())  # 'True' : car la variable 's' ne contient que des caractères alphabétiques

print(help("str"))  # Affichage de l'aide sur la chaîne de caractères

print(s.find('o'))  # '1' : la lettre 'o' se situe à l'indice 1 du str 'Bonjour'

print(s.find('o', 2))  # '4' : à partir de l'indice '2', la lettre 'o' se trouve à l'indice 4 du str 'Bonjour'

s = "madame Claude rencontre madame Dominique"

print(s.replace('madame', 'monsieur'))  # 'monsieur Claude rencontre monsieur Dominique'

print(s)  # 'madame Claude rencontre madame Dominique' : le str est inchangé malgré le recours de replace() ci-avant
s = s.replace('madame', 'monsieur')  # Cette fois-ci la variable 's' est modifiée
print(s)  # 'monsieur Claude rencontre monsieur Dominique'

print(s.capitalize())  # 'Madame claude rencontre madame dominique' : lettre majuscule pour la 1ère lettre du str

s = 'bOnjouR'

print(s.capitalize())  # 'Bonjour' : la 1ère lettre en majuscule et les autres lettres sont en minuscules

print(s.strip())  # 'Bonjour' : copie de la variable 's' en supprimant les espace en début et fin du str
