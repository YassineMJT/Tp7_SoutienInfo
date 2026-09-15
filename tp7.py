#Jeu des couleurs 

import random

game = True

liste_couleurs = {
    "R" : "Rouge",
    "B" : "Bleu",
    "V" : "Vert",
    "J" : "Jaune",
    "M" : "Mauve",
    "N" : "Noir"
}

lettres_valides = list(liste_couleurs.keys())

difficulte_explication = "1-Easy (Code de 2 couleurs à deviner), \n 2-Medium (Code de 3 couleurs à deviner) \n 3-Hard (Code de 4 couleurs à deviner)"

while game:
    code = []
    nmbre_tentative = 12
    nmbre_tour = 1
    gagne = False
    code_cache = []

    print("\nBienvenue dans le jeu des couleurs (Mastermind) ! Dans celui-ci vous devez deviner un code secret de plusieurs couleurs, parmi celle-ci, les couleurs (ou lettre) possibles sont : ")
    for lettre, nom in liste_couleurs.items():
        print(f"  {lettre} : {nom}"
        )
    print("À chaque tentative vous aurez la possibilité de deviner une couleur dans le code mais attention ! Vous n'en avez que 12.\n")

    try:
        difficulté = int(input(f"En quel difficulté souhaitez-vous jouer (Tapez le chiffre) ? \n {difficulte_explication}\n"))

        if difficulté == 1:
            nmbre_couleur = 2

        elif difficulté == 2:
            nmbre_couleur = 3

        elif difficulté == 3:
            nmbre_couleur = 4

        for _ in range(nmbre_couleur):
            code.append(random.choice(lettres_valides))

        for i in code:
            code_cache.append("*")

        print(f"A vous de deviner le code {code_cache}")

    except ValueError:
        print(f"Vous n'avez sélectionné aucune difficulté (Sélectionnez un chiffre parmi les options : \n {difficulte_explication})")
        continue

    while nmbre_tentative > 0 and not gagne:

        try:
            saisie = input(f"Tour n°{nmbre_tour}/12 : Quel est le code ? Entrez votre combinaion de lettre (R,V,J,B,N,M)").upper().replace(" ", "")

            if len(saisie) != nmbre_couleur:
                print(f"Vous n'avez pas donné un nombre de lettre égale à {nmbre_couleur}")
                continue

            if all(c not in liste_couleurs for c in saisie):
                print(
                    f"Erreur, vous avez mis des couleurs qui ne sont pas dans la liste des couleurs possible : "
                    f" {', '.join(lettres_valides)} !\n"
                )
                continue

            nmbre_tentative -= 1
            nmbre_tour += 1

            saisie_liste = list(saisie)
            code_restant = []
            saisie_restant = []

            correct = 0
            partiel = 0

            #Verification lettre correct :
            for i in range(len(code)):
                if saisie[i] == code[i]:
                    correct += 1
                else:
                    code_restant.append(code[i])
                    saisie_restant.append(saisie[i])

            #verification partiel correct :
            for lettre in saisie_restant:
                if lettre in code_restant:
                    partiel += 1
                    code_restant.remove(lettre)

            if saisie_liste == code:
                gagne = True
                print(f"Bravo vous avez trouvé toutes les couleurs en {nmbre_tour} tours\n Le résultat était bien {code}")

            print(f"Résultat -> Correct : {correct} Partiel : {partiel}\n")

        except ValueError:
            print(f"Vous n'avez pas mis {nmbre_couleur} couleurs")
    else:
        print(f"Perdu ! Le code était {code}")
        choix_recommencer = int(input("Souhaitez-vous recommencer une partie ? \n1-Oui,\n2-Non laisse moi tranquille\n"))
    if choix_recommencer == 1:
        game = True
    else:
        game = False
else:
    print("Ok merci d'avoir joué")

