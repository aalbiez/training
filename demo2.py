nom = input("comment t'appelles tu ? ")
print("bonjour %s" % nom)
age = int(input("quel age as tu ? "))
if age < 3:
    print ("tu es un bebe")
elif age <13:
    print ("tu es un(e) enfant")
elif age <18:
    print ("tu es un(e) ado")
elif age <25:
    print("tu est un(e) jeune adulte")
elif age <65:
    print("tu est un(e) adulte")
else:
    print("tu res un(e) sénior")
jeu = input("quel est ton genre de jeu video préferé ? ")
if jeu == "combat":
    print("tu as l'air d'aimer la violence.")
else:
    print("je ne connais pas mais ça à l'air super !!!!!!")
    parle = input("de quoi ça parle ? ")
    print ("tu pourras m'apprendre comment ça se joue.")
activiter = input("quel est ton activiter sportive preferé ? ")
if activiter == "foot":
    print ("j'aime aussi le foot")
elif activiter == "handball":
    print ("j' aime pas trop le handball")
elif activiter == "course":
    print ("je suis lente.")
    parles = input("Et toi?")
elif activiter == "le saut en hauteur":
    print ("moi je ne saute pas très haut.")
    haute = input("tu saute combien de mètre ?")
    if haute <1:
        print("tu saute aussi haut que moi.")
    elif haute <2:
        print ("tu saute plus haut que moi.")
    elif haute <3:
        print ("tu est un chanpion!!!!!")
    else:
        print("t'est sur de pas te tronpé ?????")
else:
    print("je ne connais pas.")
