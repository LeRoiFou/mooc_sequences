"""
Écrire une fonction transcription_arn(brin) qui reçoit une chaîne de caractères en paramètre, correspondant à un brin
d'ADN, et qui retourne une chaîne de caractère correspondant à la transcription ARN de ce brin.

Nous rappelons qu'un brin d'ADN peut être modélisé par une chaîne de caractères, dont les caractères sont pris parmi
les quatre suivants  : 'A'(Adénine), 'C' (Cytosine),'G' (Guanine) et 'T' (Thymine). La transcription en ARN se
traduit par le remplacement des nucléotides de Thymine par des nucléotides d'Uracile, que l'on représentera par le
caractère 'U'.

Exemple
L’appel suivant de la fonction :
transcription_arn('AGTCTTACCGATCCAT')
doit retourner :
'AGUCUUACCGAUCCAU'

Éditeur : Laurent REYNAUD
Date : 26-07-2020
"""


def transcription_arn(brin):
    return brin.replace("T", "U")


texte = input()
print(transcription_arn(texte))
