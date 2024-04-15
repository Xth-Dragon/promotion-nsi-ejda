# Proposer le menu d'un restaurant pour commander (avec dictionnaires)

# Importation des modules nécessaires

import random, time


# Definition des listes

suggestion = []


# Definition des dictionnaires

# Liste des entrées
entree = {
    "Salade": 10,
    "Soupe": 12,
    "Carpaccio": 14,
    "Bruschetta": 11,
    "Friture de calamars": 15,
    "Pâté en croûte": 13,
    "Velouté de champignons": 10.5
}

# Liste des plats
plat = {
    "Filet de boeuf": 25,
    "Risotto": 18,
    "Poulet": 20,
    "Saumon grillé": 22,
    "Pâtes aux fruits de mer": 19,
    "Magret de canard": 24,
    "Burger gourmet": 16.5
}

# Liste des desserts
dessert = {
    "Tiramisu": 7,
    "Fondant au chocolat": 9,
    "Crème brulée": 8,
    "Mousse au citron": 6.5,
    "Tarte aux fruits rouges": 10,
    "Profiteroles": 8.5,
    "Café gourmand": 11
}

# Liste des vins

vin = {
    "Vin 1" : 12,
    "Vin 2" : 18,
    "Vin 3" : 25,
    "Vin 4" : 50,
    "Vin 5" : 75
}

# Definition de la fonction principale

def commandes():

    # Message de bienvenue

    print("\n||| Bienvenue !! |||\n\n")
    print("***Menu suggéré***")

    # Suggestion d'une entrée, d'un  plat et d'un dessert

    entree_suggestion = random.choice(list(entree.keys()))
    plat_suggestion = random.choice(list(plat.keys()))
    dessert_suggestion = random.choice(list(dessert.keys()))
    vin_suggestion = random.choice(list(vin.keys()))

    prix_suggestions = entree[entree_suggestion] + plat[plat_suggestion] + dessert[dessert_suggestion] + vin[vin_suggestion]


    print(f"- Suggestion d'entrée : {entree_suggestion}")
    print(f"- Suggestion de plat : {plat_suggestion}")
    print(f"- Suggestion de dessert : {dessert_suggestion}")
    print(f"- Suggestion de vin : {vin_suggestion}")
    print(f"Prix du menu suggéré : {prix_suggestions} € ")

    # Permet de mettre un temps de pause
    time.sleep(1)

    suggestion_du_jour = input("\n\nSi vous souhaitez prendre les suggestions du jour, rentrez '0', sinon appuyez sur une autre touche\nVotre choix :  ")
    print()

    if suggestion_du_jour == "0":
        entree_prise = entree_suggestion
        plat_pris = plat_suggestion
        dessert_pris = dessert_suggestion
        vin_pris = vin_suggestion

    else:


        # Permet de mettre un temps de pause
        time.sleep(1)


        # Affichage du menu

        print("||| Voici le menu : ")

        print("\nEntrées : ")
        for cle, valeur in entree.items():
            print(f"- {cle}, Prix: {valeur}")

        print("\nPlat: ")
        for cle, valeur in plat.items():
            print(f"- {cle}, Prix: {valeur}")

        print("\nDessert : ")
        for cle, valeur in dessert.items():
            print(f"- {cle}, Prix: {valeur}")

        print("\nVin : ")
        for cle, valeur in vin.items():
            print(f"- {cle}, Prix: {valeur}")

        time.sleep(1)

        # Permet de laisser un court temps de pause

        print("\nAvez vous fait votre choix ?")

        time.sleep(1)

        # Lancement de la partie "commande"

        print("\n\n||| Lancement de la commande : ")


        entree_prise = input("Rentrez l'entrée désirée\nSi vous ne souhaitez pas prendre d'entrée, rentrez '0'\nEntrée désirée : ")
        print()

        if entree_prise in entree.keys():
            print("Entrée commandée avec succès !")
        elif entree_prise == "0":
            print("Vous avez choisi de ne pas prendre d'entrée !")
        else:
            print("Commande invalide !!")
        print()


        plat_pris = input("Rentrez le plat désiré\nSi vous ne souhaitez pas prendre de plat, rentrez '0'\nPLat désiré : ")
        print()

        if plat_pris in plat.keys():
            print("Plat commandé avec succès !")
        elif plat_pris == "0":
            print("Vous avez choisi de ne pas prendre de plat !")
        else:
            print("Commande invalide !!")
        print()


        dessert_pris = input("Rentrez le dessert désiré\nSi vous ne souhaitez pas prendre de dessert, rentrez '0'\nDessert désiré : ")
        print()
        if dessert_pris in dessert.keys():
            print("Dessert commandé avec succès !")
        elif dessert_pris == "0":
            print("Vous avez choisi de ne pas prendre de dessert !")
        else:
            print("Commande invalide !!")
        print()


        vin_pris = input("Rentrez le vin désiré\nSi vous ne souhaitez pas prendre de vin, rentrez '0'\nVin désiré : ")
        print()
        if vin_pris in vin.keys():
            print("Vin commandé avec succès !")
        elif vin_pris == "0":
            print("Vous avez choisi de ne pas prendre de vin !")
        else:
            print("Commande invalide !!")
        print()

    # Calcul de l'addition

    if entree_prise in entree:
        prix_entree = entree[entree_prise]
    else:
        prix_entree = 0

    if plat_pris in plat:
        prix_plat = plat[plat_pris]
    else:
        prix_plat = 0

    if dessert_pris in dessert:
        prix_dessert = dessert[dessert_pris]
    else:
        prix_dessert = 0

    if vin_pris in vin:
        prix_vin = vin[vin_pris]
    else:
        prix_vin = 0



    total_prix = prix_entree + prix_plat + prix_dessert + prix_vin


    # Affichage de l'addition

    print("Voici l'addition : \n")

    if entree_prise in entree:
        print(f"* Entree : {entree_prise}, prix : {entree[entree_prise]} €")
    else:
        print("* Vous n'avez pas pris d'entrée")

    print()

    if plat_pris in plat:
        print(f"* Plat : {plat_pris}, prix : {plat[plat_pris]} €")
    else:
        print("* Vous n'avez pas pris de plat")

    print()

    if dessert_pris in dessert:
        print(f"* Dessert : {dessert_pris}, prix : {dessert[dessert_pris]} €")
    else:
        print("* Vous n'avez pas pris de dessert")

    print()

    if  vin_pris in vin:
        print(f"* Vin : {vin_pris}, prix : {vin[vin_pris]} €")
    else:
        print("* Vous n'avez pas pris de vin")

    print()


    print(f"Voici le prix à payer : {total_prix} €")




# Appel a le fonction directrice afin de lancer le programme

commandes()


# Permet au programme de s'eteinder après que l'utilisateur l'est choisi ( si le programme est compilé sinon c'est inutile)

while True:
    print()
    print()
    fin = input("!! Fin du programme !!\n- Rentrez 0 pour relancer le programme\n- Appuyez sur n'importe quelle autre touche pour quitter le programme\nVotre choix : ")

    if fin == "0":
        print()
        print()
        commandes()
    else:
        print("Fermeture du programme")
        break



