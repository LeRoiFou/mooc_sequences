"""
Le découpage en tranches : slicing 
Cela consiste à récupérer une sous-séquence de la séquence d'origine 

Éditeur : Laurent REYNAUD 
Date : 25-07-2020 
"""

s = "Bonjour, ça va ?"

print(s[1:3])  # "on" -> la composante d'indice 3 est exclue (donc "j"), ce qui revient à s[1:3[

print(s[:3])  # "Bon" -> va du début de la séquence à l'indice 3 exclu

print(s[1:])  # "onjour, ça va ?" -> va du 1er indice de la séquence jusqu'à la fin INCLUS

prem = [2, 3, 5, 7, 9]

sec = prem[:]  # découpage en tranches sans préciser le 1er ni le dernier indice -> copie de la liste en question
print(sec)  # "[2, 3, 5, 7, 9]"

text = "Bonjour"

print(text[::2])  # "Bnor" -> affichage de la chaîne de caractères par pas de 2

print(text[::-1])  # "ruojnoB" -> affichange de la chaîne de caractères en partant de la fin
