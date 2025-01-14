import random

def shifumi():
    choix = ["pierre", "feuille", "ciseaux", "lézard", "Spock"] # liste des choix possibles
    machine_choice = random.randint(0, 4) # machine choisit un nombre aléatoire entre 0 et 4 qui correspond à la position dans la liste des différentes armes
    player_choice = input("Choisissez entre pierre, feuille, ciseaux, lézard ou Spock: ") # joueur choisit une arme parmi les cinq possibles
    print(f"La machine a joué {choix[machine_choice]} et vous avez joué {player_choice}")
    
    if player_choice == "pierre":
        if choix[machine_choice] == "pierre":
            print("Égalité")
        elif choix[machine_choice] in ["feuille", "Spock"]:
            print(f"{choix[machine_choice]} gagne contre {player_choice}!")
        else:
            print(f"{player_choice} gagne contre {choix[machine_choice]}!")
    
    elif player_choice == "feuille":
        if choix[machine_choice] == "feuille":
            print("Égalité")
        elif choix[machine_choice] in ["ciseaux", "lézard"]:
            print(f"{choix[machine_choice]} gagne contre {player_choice}!")
        else:
            print(f"{player_choice} gagne contre {choix[machine_choice]}!")
    
    elif player_choice == "ciseaux":
        if choix[machine_choice] == "ciseaux":
            print("Égalité")
        elif choix[machine_choice] in ["pierre", "Spock"]:
            print(f"{choix[machine_choice]} gagne contre {player_choice}!")
        else:
            print(f"{player_choice} gagne contre {choix[machine_choice]}!")
    
    elif player_choice == "lézard":
        if choix[machine_choice] == "lézard":
            print("Égalité")
        elif choix[machine_choice] in ["pierre", "ciseaux"]:
            print(f"{choix[machine_choice]} gagne contre {player_choice}!")
        else:
            print(f"{player_choice} gagne contre {choix[machine_choice]}!")
    
    elif player_choice == "Spock":
        if choix[machine_choice] == "Spock":
            print("Égalité")
        elif choix[machine_choice] in ["feuille", "lézard"]:
            print(f"{choix[machine_choice]} gagne contre {player_choice}!")
        else:
            print(f"{player_choice} gagne contre {choix[machine_choice]}!")
    else:
        print("Choix invalide. Veuillez choisir entre pierre, feuille, ciseaux, lézard ou Spock.")

# Exécuter la fonction
shifumi()
