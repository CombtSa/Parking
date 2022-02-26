parking = {}
parking[0] = ""
parking[1] = ""
parking[2] = ""
parking[3] = ""
parking[4] = ""
parking[5] = ""
parking[6] = ""
parking[7] = ""
parking[8] = ""
parking[9] = ""
parking[10] = ""

nom = input('Quel est votre nom')
place_voiture = input('Quel place voulait vous prendre ? de 1 à 10')

with open("donne.txt", "a", encoding="utf8") as fichier:
    if place_voiture == '1':
        parking[1] = nom
        fichier.write("cette place appartient à : ")
        fichier.write(str(parking[1]))
    elif parking[1] == nom:
        fichier.read(int(parking[1]))

    if place_voiture == '2':
        parking[2] = nom
        fichier.write("cette place appartient à : ")
        fichier.write(str(parking[2]))
    elif parking[2] == nom:
        fichier.read(int(parking[2]))

    if place_voiture == '3':
        parking[3] = nom
        fichier.write("cette place appartient à : ")
        fichier.write(str(parking[3]))
    elif parking[3] == nom:
        fichier.read(int(parking[3]))

    if place_voiture == '4':
        parking[4] = nom
        fichier.write("cette place appartient à : ")
        fichier.write(str(parking[4]))
    elif parking[4] == nom:
        fichier.read(int(parking[4]))

    if place_voiture == '5':
        parking[5] = nom
        fichier.write("cette place appartient à : ")
        fichier.write(str(parking[5]))
    elif parking[5] == nom:
        fichier.read(int(parking[5]))
