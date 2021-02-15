"""
Manipulation des fichiers texte
Les instructions ci-après permettent l'ouverture, la lecture et la fermeture d'un fichier texte
Éditeur : Laurent REYNAUD
Date : 01-08-2020
"""
""" 
Ouverture d'un fichier afin de pouvoir le lire par la suite : 
Ne pas oublier de mettre l'instruction 'encoding=""' pour que le fichier puisse lire correctement les caractères 
spécifiques tels que les 'é', 'è', 'ç'... 
"""
mon_fichier = open("pieces/Test.txt", encoding="utf-8")
""" 
L'instruction ci-après permet de lire la 1ère ligne du fichier 
"""
print(mon_fichier.readline())
""" 
L'instruction ci-après permet de fermer le fichier ouvert, qui met fin au lien avec l'application Python 
"""
mon_fichier.close()
""" 
Les instructions ci-après permettent de lire les 3 premières lignes du fichier 
"""
mon_fichier = open("pieces/Test.txt", encoding="utf-8")
print(mon_fichier.readline().strip())
print(mon_fichier.readline().strip())
print(mon_fichier.readline().strip())
mon_fichier.close()
""" 
Autre solution pour lire toutes les lignes du fichier 
"""
mon_fichier = open("pieces/Test.txt", encoding="utf-8")
for ligne in mon_fichier:
    print(ligne.strip())
print(type(mon_fichier))  # Type du fichier : <class '_io.TextIOWrapper'>
mon_fichier.close()
