place = {}
place[1] = ""
place[2] = ""
place[3] = ""
place[4] = ""
place[5] = ""
place[6] = ""
place[7] = ""
place[8] = ""
place[9] = ""
place[10] = ""

while True:
    num_actu = 1
    place_actu = print("Vous etes devant la place", num_actu)
    choix_user = input('1- placer votre voiture 2- Prendre votre voiture')

    if place[num_actu] == "Libre":
        print(choix_user)
    if choix_user == '1':
        place[num_actu] = "Occupé"
    elif place[num_actu] == "Occupe":
        num_actu += 1
    else:
        print("La place est inexistante ")







