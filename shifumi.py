import random

def shifumi():
    choix = ["pierre", "feuille", "ciseaux", "lézard", "Spock"] # liste des choix possibles
    machine_choice = random.randint(0, 4) # machine choisit un nombre aléatoire entre 0 et 4
    player_choice = input("Choisissez entre pierre, feuille, ciseaux, lézard ou Spock: ") # joueur choisit une arme parmi les cinq possibles
    print(f"La machine a joué {choix[machine_choice]} et vous avez joué {player_choice}")
    
    if player_choice == choix[machine_choice]:
        print("Égalité")
    else:
        if (player_choice == "pierre" and (choix[machine_choice] == "ciseaux" or choix[machine_choice] == "lézard")) or \
           (player_choice == "feuille" and (choix[machine_choice] == "pierre" or choix[machine_choice] == "Spock")) or \
           (player_choice == "ciseaux" and (choix[machine_choice] == "feuille" or choix[machine_choice] == "lézard")) or \
           (player_choice == "lézard" and (choix[machine_choice] == "feuille" or choix[machine_choice] == "Spock")) or \
           (player_choice == "Spock" and (choix[machine_choice] == "pierre" or choix[machine_choice] == "ciseaux")):
            print(f"{player_choice} gagne contre {choix[machine_choice]}!")
        else:
            print(f"{choix[machine_choice]} gagne contre {player_choice}!")

# Exécuter la fonction
shifumi()
