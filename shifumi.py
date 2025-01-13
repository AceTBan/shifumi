import random
def shifumi():
    choix = ["pierre", "feuille", "ciseaux"] #liste des choix possibles
    machine_choice = random.randint(0,2) #machine choisi un nombre aleatoire entre 0 et 2 qui correspond a la position dans la liste des differentes armes
    player_choice = input("Choisissez entre pierre, feuille ou ciseaux: ") #joueur choisi une arme parmi les trois possibles
    print(f"La machine a joué {choix[machine_choice]} et vous avez joué {player_choice}")
    
    if player_choice == "pierre":
        if machine_choice == 0:
            print("Egalite")
        elif machine_choice == 1:
            print(f"{choix[machine_choice]} gagne contre {player_choice}!")
        else:
            print(f"{player_choice} gagne contre {choix[machine_choice]}!")
    elif player_choice == "feuille":
        if machine_choice == 1:
            print("Egalite")
        elif machine_choice == 2:
            print(f"{choix[machine_choice]} gagne contre {player_choice}!")
        else:
            print(f"{player_choice} gagne contre {choix[machine_choice]}!")
    else:
        if machine_choice == 2:
            print("Egalite")
        elif machine_choice == 0:
            print(f"{choix[machine_choice]} gagne contre {player_choice}!")
        else:
            print(f"{player_choice} gagne contre {choix[machine_choice]}!")