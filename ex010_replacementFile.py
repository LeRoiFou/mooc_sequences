"""
Écrire une fonction nouveaux_heros dont le but consiste à remplacer les héros d'une histoire.

La fonction acceptera deux paramètres : le premier sera une chaîne de caractères précisant le nom du fichier
contenant l'histoire initiale ; le deuxième sera une chaîne de caractères précisant le nom du fichier dans lequel
sera sauvegardée l'histoire modifiée comme précisé ci-dessous.

Dans l'histoire initiale, présente dans le fichier dont le nom est donné en premier argument, trois protagonistes
interviennent : Pierre, Paul et Jacqueline. La fonction devra remplacer ces trois héros par, respectivement, Paul,
Tom et Mathilde. Le texte ainsi modifié sera alors stocké dans le fichier dont le nom est donné en deuxième argument.
Aucune autre modification ne sera apportée au texte initial.

Exemple
Sachant que le fichier histoire_1.txt contient le texte :
Si Pierre est le fils de Paul, et si Paul est le frère de Jacqueline, qui est Pierre pour Jacqueline ?
après l'appel suivant de la fonction :
nouveaux_heros("histoire_1.txt", "nouvelle_histoire_1.txt")
le fichier dont le nom est nouvelle_histoire_1.txt doit contenir le texte :

Si Paul est le fils de Tom, et si Tom est le frère de Mathilde, qui est Paul pour Mathilde ?

Conseils :

Pour tester votre fonction, assurez-vous de copier le fichier à lire dans le répertoire courant (ou de passer comme
argument le chemin complet vers le fichier).

L’utilisation de la méthode replace sur les chaînes de caractères va s’avérer très utile. Mais attention à Paul qui
se trouve à la fois dans les anciens héros et les nouveaux. Une façon de procéder pourrait consister à remplacer,
provisoirement, la chaîne "Paul" par une autre valeur (attention toutefois à ce que cette valeur provisoire ne soit
pas elle-même présente dans le texte).

Éditeur : Laurent REYNAUD
Date : 02-08-2020
"""


def nouveaux_heros(fichier_initial, fichier_modifie):
    f = open(fichier_initial, encoding="utf-8")
    fichier_lu = f.read()
    f.close()

    f = open(fichier_modifie, 'w')
    f1 = fichier_lu.replace("Paul", "Tom")
    f.close()

    f = open(fichier_modifie, 'w')
    f1 = f1.replace("Pierre", "Paul")
    f.close()

    f = open(fichier_modifie, 'w')
    f.write(f1.replace("Jacqueline", "Mathilde"))
    f.close()


print("Chemin du fichier initial : pieces/histoire_1.txt")
fichier1 = input()
print("Chemin du fichier modifié : pieces/histoire_11.txt")
fichier2 = input()
nouveaux_heros(fichier1, fichier2)
