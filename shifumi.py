import random  # Importer la bibliothèque random pour générer des choix aléatoires

def shifumi():
    choix = ["pierre", "feuille", "ciseaux", "lézard", "Spock"]  # Liste des choix possibles
    machine_choice = random.randint(0, 4)  # La machine choisit un nombre aléatoire entre 0 et 4
    player_choice = input("Choisissez entre pierre, feuille, ciseaux, lézard ou Spock: ")  # Le joueur choisit une arme parmi les cinq possibles
    print(f"La machine a joué {choix[machine_choice]} et vous avez joué {player_choice}")  # Afficher les choix de la machine et du joueur
    
    if player_choice == choix[machine_choice]:
        print("Égalité")  # Vérifier si les choix sont identiques, auquel cas c'est une égalité
    else:
        # Vérifier toutes les combinaisons gagnantes pour le joueur
        if (player_choice == "pierre" and (choix[machine_choice] == "ciseaux" or choix[machine_choice] == "lézard")) or \
           (player_choice == "feuille" and (choix[machine_choice] == "pierre" or choix[machine_choice] == "Spock")) or \
           (player_choice == "ciseaux" and (choix[machine_choice] == "feuille" ou choix[machine_choice] == "lézard")) or \
           (player_choice == "lézard" and (choix[machine_choice] == "feuille" ou choix[machine_choice] == "Spock")) ou \
           (player_choice == "Spock" and (choix[machine_choice] == "pierre" ou choix[machine_choice] == "ciseaux")):
            print(f"{player_choice} gagne contre {choix[machine_choice]}!")  # Annoncer la victoire du joueur
        else:
            print(f"{choix[machine_choice]} gagne contre {player_choice}!")  # Annoncer la victoire de la machine

# Exécuter la fonction
shifumi()
