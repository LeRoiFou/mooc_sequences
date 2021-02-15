
"""
Manipulation des fichiers texte
Les instructions ci-après permettent d'effectuer des recherches dans un fichier

Éditeur : Laurent REYNAUD
Date : 01-08-2020
"""
""" 
L'instruction with open() as .. ouvre un fichier pour traitement à l'intérieur du with et avec l'instruction with, le 
fichier est proprement fermé 
"""
with open("pieces/Test.txt", encoding="utf-8") as mots:
    for m in mots:
        if len(m) > 24:  # Recherche toutes les lignes qui ont + de 24 caractères (dont les espaces)
            print(m.strip())
""" 
L'instruction for .. in open () ouvre et traite chaque ligne de fichier et le ferme à la fin du for 
"""
for m in open("pieces/Test.txt", encoding="utf-8"):
    if "rr" in m and "ss" in m and "tt" in m:  # Recherche toutes lignes comprenant ces caractères
        print(m.strip())
""" 
L'instruction f = open(.., "w", encoding="utf-8") permet d'écrire dans le fichier concerné et de remplacer toutes les 
saisies précédentes dans ce fichier 
"""
f = open("pieces/Test.txt", "w", encoding="utf-8")
f.write("Bonjour :) \n")
f.write("165 \n")  # Les chiffres doivent être en format str
f.close()
""" 
L'instruction f = open(.., "a", encoding="utf-8") permet d'écrire dans le fichier concerné et d'ajouter toutes les 
saisies précédentes dans ce fichier 
"""
f = open("pieces/Test.txt", "a", encoding="utf-8")
f.write("Bonjour bis:) \n")
f.write("Coucou 657 bis! \n")
f.close()
f_in = input("fichier de données : ")
f_out = input("fichier de résultats : ")
with open(f_out, 'w', encoding='utf-8') as r:
    deja_vu = set()                           # deja_vu est l'ensemble vide
    for texte in open(f_in, encoding='utf-8'):
        if texte not in deja_vu:
            deja_vu |= {texte}                # ajoute texte à l'ensemble deja_vu
            r.write(texte)
