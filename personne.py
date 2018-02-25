# -*- coding: utf-8 -*-

from datetime import date, datetime



class Personne:
    def __init__(self, nom, prenom, naissance):
        self.nom = nom
        self.prenom = prenom
        self.naissance = naissance

    def initiales(self):
        return self.prenom[0] + self.nom[0]

    def trigram(self):
        return (self.prenom[0] + self.nom[0] + self.nom[1]).upper()

    def age(self, aujourdhui):
        return (aujourdhui - self.naissance).days / 365

    def __repr__(self):
        return "<Personne(" + self.nom + ")>"


arnaud = Personne("Albiez", "Arnaud", date(2002, 11, 26))
print arnaud.age(date.today())


start = datetime.now()
v = raw_input("> ")
stop = datetime.now()
print stop - start
