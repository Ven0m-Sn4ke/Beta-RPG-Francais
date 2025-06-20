import random 
import time
import sys
print("== Beta RPG ver 0.0.1 ==")

x = ""
while x == "":
    x = input("Entrez nom peronnage : ")

print(f"Bienvenue {x}")
h = 100
m = 0
stuff_weapon = []
stuff_object = []
bete_masion_voisine = True
maison_voisine2 = True
carte_des_villages = False
sk = False

print(r'''  _____           _                              _                  _ _ _                  
 |  __ \         | |                         _  | |                (_) | |                 
 | |__) | __ ___ | | ___   __ _ _   _  ___  (_) | |     ___  __   ___| | | __ _  __ _  ___ 
 |  ___/ '__/ _ \| |/ _ \ / _` | | | |/ _ \     | |    / _ \ \ \ / / | | |/ _` |/ _` |/ _ \
 | |   | | | (_) | | (_) | (_| | |_| |  __/  _  | |___|  __/  \ V /| | | | (_| | (_| |  __/
 |_|   |_|  \___/|_|\___/ \__, |\__,_|\___| (_) |______\___|   \_/ |_|_|_|\__,_|\__, |\___|
                           __/ |                                                 __/ |     
                          |___/                                                 |___/      
''')

time.sleep(2)

def fiche_perso():
    print(f"\n== Fiche de personnage de {x} ==")
    print(f"Santé : {h}")
    print(f"Argent : {m}")
    print(f"Inventaire (arme) : {stuff_weapon}")
    print(f"Inventaire (objet) : {stuff_object}")
    l = len(x)
    z = "=" * l
    print(f"============================={z}")

def maison1():
    print("\nVous vous trouvez actuellement chez vous, vous vous reveillez d'une bonne nuit de sommeil, que decidez vous de faire ? ")
    print("1 : Sortir de chez vous")
    print("2 : Vous recouchez")
    print("3 : Fouillez votre maison")
    print("4 : Afficher fiche de personnage ")
    xc = ""
    global sk
    fini = False
    while not fini :
        xc = input("Votre choix : ")
        if xc == "1" :
            print("\nVous sortez de chez vous")
            fini = True
        if xc == "2" :
            print("\nVous vous etes assez reposez") 
        if xc == "3" :
            if sk == False :
                print("\nEn fouyant votre maison, vous trouvez un couteau dont la lameest émmoussée, pas très puissant mais peut s'averer utile")
                print("'Couteau abîmé' a été ajouté a votre inventaire")
                stuff_weapon.append("Couteau abîmé")
                sk = True
            else :
                print("\nIl n'y a plus rien d'interessnt dans votre maison")
        if xc == "4" :
            fiche_perso()

def maison2():
    xm2 = ""
    global sk
    print("\nVous etes de retour chez vous")
    print("Que faites vous ?")
    print("1 : Vous vous recouchez")
    print("2 : Vous fouillez la maison")
    print("3 : Vous resortez")
    print("4 : Afficher fiche du personnage")
    while True :
        xm2 = input("Votre choix : ")
        if xm2 == "1" :
            print("\nVous vous etes assez reposez")
        if xm2 == "2" :
            if sk == False :
                print("\nEn fouyant votre maison, vous trouvez un couteau dont la lameest émmoussée, pas très puissant mais peut s'averer utile")
                print("'Couteau abîmé' a été ajouté a votre inventaire")
                stuff_weapon.append("Couteau abîmé")
                sk = True
            else :
                print("\nIl n'y a plus rien d'interessnt dans votre maison")
        if xm2 == "3" :
            devant_maison_village()
        if xm2 == "4" : 
            fiche_perso()
 

def devant_maison_village():
    print("\nVous etes de retour devant chez vous")
    print("Que faites vous ?")
    print("1 : Retournez sur les lieux des hurlements")
    print("2 : Vous tentez de penetrer une maison abandonné")
    print("3 : Vous retournez chez vous")
    print("4 : Vous quitez le village")
    print("5 : Afficher fiche de personnage")
    while True :
        xdmv = input("Votre choix : ")
        if xdmv == "1" :
            maison_voisine()
        if xdmv == "2" :
            print("\nApres moultes tentatives vous finissez par forcer une portes des maisons")
            maison_pénétrée()
        if xdmv == "3" :
            print("\nVous retournez chez vous")
            maison2()
        if xdmv == "4" :
            if 'Carte des villages' in stuff_object :
                print("\nApres avoir fais face a l'horreur qui a frappé votre village et recupéré la carte des villages, vous etes desormais en route")
                print("pour chercher de l'aide et des informations sur ce qui s'est passé ici...")
                time.sleep(2)
                print("\nA suivre...")
                sys.exit()
            else :
                print("\nVous ne savez pas où allez, essayer de trouver quelque chose pour indiquer votre chemin")
        if xdmv == "5" :
            fiche_perso()


def maison_pénétrée():
    global carte_des_villages
    global h
    print("\nVous etes desormais a l'interieur d'une des maisons")
    print("Que faites vous ?")
    print("1 : Resortir")
    print("2 : Fouiller")
    print("3 : Utiliser la clé ('Clé cave' necessaire)")
    print("4 : Afficher fiche de personnage")
    while True :
        xmp = input("Votre choix :  ")
        if xmp == "1" :
            devant_maison_village()
        if xmp == "2" :
            print("\nEn fouillant dans la maison, vous trouvez divers objet comme des ustensiles de cuisine ou des vetements... ")
            print("C'est là que vous tombez nez à nez avec une sorte de cote de maille en parfait etat, parfait pour se prtéger")
            print("'Armure cote de maille a été ajouté a votre inventaire'")
            h = h + 30
        if xmp == "3" :
            if 'Clé cave' in stuff_object :
                print("\nVous remarquez dans la maison une porte vérouillée, vous utilisez donc la clé préalablement récupérée sur")
                print("le corps de votre voisine, en entrant dans la cave vous découvrez une carte menant aux autres villages alliés au votre")
                print("vous décidez donc de partir pour avertir les autres de la menace...")
                stuff_object.append("Carte des villages")
                carte_des_villages = True
            else :
                print("\nImpossible d'ouvrir la porte de la cave... Vous n'avez pas la clé")
        if xmp == "4" : 
            fiche_perso()


def maison_voisine():
    global bete_masion_voisine
    global maison_voisine2
    fini2 = False
    if bete_masion_voisine == True :
        global sk
        global h
        print("\nC'est le moment d'agir ! Votre voisine est en danger il faut faire quelque chose !")
        print("1 : Vous attaquez la creature")
        print("2 : Vous tentez de distraire la créature en lencant une boite a l'opposé de la direction de ta voisine")
        print("3 : Afficher fiche de personnage")
        xc2_1 = ""
        while not fini2 :
            xc2_1 = input("Votre choix : ")
            if xc2_1 == "1" :
                if sk == True :
                    print("\nous sortez votre couteau abîmé et vous ruez sur la créature et lui plantez votre lame dans plusieurs parties du corps")
                    print("Heuresement la créature se vide de son sang et meurt")
                    print("Malheuresement la lame de votre couteau se brise, vous perdez donc votre couteau")
                    sk = 0
                    stuff_weapon.remove("Couteau abîmé")
                    fini2 = True
                    bete_masion_voisine = False
                    bete
                else :
                    print("\nVous vous ruez sur la créature pour lui mettre des coups de point et pieds mais elle tente quand même de se debattre et vous")
                    print("inflige quelques blessure aux bras et aux jambes")
                    h = h-20
                    fini2 = True
                    bete_masion_voisine = False
            if xc2_1 == "2" : 
                print("\nVous attrapez une boîte de conserve et la lancez de toutes vos forces a l'opposé de là où se trouve votre voisine, fort heuresement")
                print("la créature est distraite par le bruit et se dirge dans cette direction")
                fini2 = True
                bete_masion_voisine = False
            if xc2_1 == "3" :
                fiche_perso()
    else :        
        print("\nAprès vous etes débarassé de la bête, vous allez voir si votre voisine s'en est sorti, malheuresement celle ci aura sucombée")
        print("à ses blessures qui de toutes façon n'était pas guerissable...")
        print("Que faites vous ?")
        print("1 : Fouiller le corps de votre voisine")
        print("2 : Retourner devant chez vous")
        print("3 : Rentrer dans la maison de votre voisine")
        print("4 : Afficher fiche de peronnage")

        fini3 = False
        corps_voisine = True
        maison_voisine2 = True
        while not fini3 :
            xc2_2 = input("Votre choix : ")
            if xc2_2 == "1" :
                if corps_voisine ==  True :
                    print("\nVous vous approchez du corps encore chaud de votre voisine sur lequel vous trouvez une clé avec gravée dessus 'cave'")
                    print("'Clé cave' à été ajoutée a votre inventaire")
                    stuff_object.append("Clé cave")
                    corps_voisine = False
                else :
                    print("\nCe corps a déjà été fouillé")
            if xc2_2 == "2" :
                print("\nVous retournez devant chez vous")
                devant_maison_village()
            if xc2_2 == "3" :
                if maison_voisine2 == True :
                    print("\nVous entrez dans la maison de votre voisine, vous ne trouvez rien de vraiment interessant ormis un couteau de cuisine")
                    print("en bien très bon état")
                    print("'Couteau cuisine' a été ajouté a votre inventaire")
                    stuff_weapon.append("Couteau cuisine")
                    maison_voisine2 = False
                else :
                    print("\nVous avez déjà fouillez la maison")
            if xc2_2 == "4" :
                fiche_perso()

maison1()

print("\nUne fois dehors, vous vous redez compte qu'il n'y a plus personnes dans les rues de votres petits villages")
print("Au loins vous entendez des cris, probablement d'origines humaines, que faites vous ?")
print("1 : Aller en direction des voix humaines")
print("2 : Aller à l'opposé de ces voix")
print("3 : Fouillez les maisons aux alentours")
print("4 : Afficher fiche de personnage")
xc1 = ""
xc2 = ""
fini1 = False
while not fini1 :
    xc1 = input("Votre choix : ")
    if xc1 == "1" :
        print("\nVous arrivez à l'endroit approximatif d'où venaient les voix humaines, c'est en arrivant sur les leiux que vous voyez")
        print("une créature tout droit sorti des enfer, d'une couleur rouge sang, des tripes lui sortant du corps, une mâchoire remplies")
        print("de dents accerées capable de broyer de l'os humains et de la taille d'un chien immense_")
        print("Heuresement la créature ne vous a pas vu, vous etes cachés derieres une maison, c'est là que vous comprnez d'où viennent")
        print("les cris, c'est une de vos voisines qui prend peur face à la bete qui tente de l'attaquer")
        xc2 = "1"
        fini1 = True
    if xc1 == "2" :
        print("\nMalgré les cris, vous partez dans la direction opposé, vous tombez face à face avec des corps calcinés desquels emmane ")
        print("de la fumée, ce qui signifie qu'ils on été brulée il y a tres peu de temps")
        print("Il n'y a rien d'interessant ici vous retournez sur vos pas...")
    if xc1 == "3" :
        print("\nVous décidez de rentrer dans les maisons aux alentours mais les portes semblent verouliées, vous abandonnez cette idée")
    if xc1 == "4" :
        fiche_perso()
    fini2 = False
   
if xc2 == "1" :
    maison_voisine()
    maison_voisine()
    
            

