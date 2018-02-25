#!/usr/bin/python
# -*- coding: UTF8 -*-

PrenomConnus = {
    'ARNAUD': "Sympa comme prénom, tu dois être un garçon.",
    'OLIVIER': "Tu dois être un mec génial.",
    'CLAIRE': 'Tu es une fille.'
}

while True:
    prenom = input("Quel est ton prénom ? ").upper()

    if prenom in PrenomConnus:
        print(PrenomConnus[prenom])
    else:
        print("Bonjour %s, je ne connais pas ton prénom." % prenom)
