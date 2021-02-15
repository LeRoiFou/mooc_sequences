"""
Écrire une fonction print_mat(M) qui reçoit une matrice M en paramètre et affiche son contenu.  

Les éléments d’une même ligne de la matrice seront affichés sur une même ligne, et séparés par une espace,  
les éléments de la ligne suivante étant affichés sur une nouvelle ligne.  

Exemple  
L’appel suivant de la fonction :  
print_mat([[1, 2], [3, 4], [5, 6]])  
doit afficher :  
1 2  
3 4  
5 6  

Consignes  
Important : Afin de permettre à UpyLaB de tester votre fonction, votre code contiendra  
également, après le code de la définition de la fonction print_mat, les instructions suivantes :  
ma_matrice = eval(input())  
print_mat(ma_matrice)  
Si la matrice vide [] est passée en argument , la fonction affiche une ligne vide.  

Dans cet exercice, la présence d’espaces en fin de ligne ne sera pas sanctionnée. Par contre, veillez à ce qu’il n’y  
ait pas de ligne supplémentaire.  

Éditeur : Laurent REYNAUD  
Date : 10-08-2020  
"""


def print_mat(M):
    if not M:
        print("")
    else:
        for i in M:
            Stri = " ".join(str(_) for _ in i)
            print(Stri)


print("Saisir : [[1, 2], [3, 4], [5, 6]]")
print("Résultat attendu :")
print("1 2")
print("3 4")
print("5 6")
ma_matrice = eval(input())
print_mat(ma_matrice)
