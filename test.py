import random
import os

# Configuration du jeu
serpents = {14: 4, 28: 10, 43: 1, 47: 18, 51: 31, 68: 33, 63: 39, 77: 26, 83: 58, 95: 53, 90: 70, 99: 80}
echelles = {2: 20, 8: 30, 16: 37, 27: 69, 47: 55, 41: 62, 73: 94, 65: 79}

MODE_AFFICHAGE = True

def afficher(message):
    if MODE_AFFICHAGE:
        print(message)

def lancer_de():
    return random.randint(1, 6)

def avancer(joueurs, joueur_actuel, valeur_de, stats):
    ancienne_pos = joueurs[joueur_actuel]
    nouvelle_position = ancienne_pos + valeur_de

    # Gestion du dépassement de la case 100
    if nouvelle_position > 100:
        reculement = nouvelle_position - 100
        afficher(f" => Le joueur {joueur_actuel + 1} dépasse 100 et recule de {reculement}")
        nouvelle_position = 100 - reculement
        stats["depassements"][joueur_actuel] += 1

    # Vérification des Serpents
    if nouvelle_position in serpents:
        destination = serpents[nouvelle_position]
        afficher(f"SNAKE ! {nouvelle_position} -> {destination}")
        nouvelle_position = destination
        stats["serpents"][joueur_actuel] += 1
    
    # Vérification des Échelles
    elif nouvelle_position in echelles:
        destination = echelles[nouvelle_position]
        afficher(f"ECHELLE ! {nouvelle_position} -> {destination}")
        nouvelle_position = destination
        stats["echelles"][joueur_actuel] += 1

    joueurs[joueur_actuel] = nouvelle_position
    return nouvelle_position

def afficher_plateau(joueurs):
    afficher("\n" + "-"*30)
    afficher("POSITIONS ACTUELLES :")
    for i, pos in enumerate(joueurs):
        leader = " (en tête)" if pos == max(joueurs) and pos > 0 else ""
        afficher(f"Joueur {i+1} : {pos}{leader}")
    afficher("-"*30)

def jouer_une_partie(nb_joueurs):
    joueurs = [0] * nb_joueurs
    tours = [0] * nb_joueurs
    stats = {
        "serpents": [0] * nb_joueurs,
        "echelles": [0] * nb_joueurs,
        "depassements": [0] * nb_joueurs
    }
    
    joueur_actuel = 0
    while True:
        if MODE_AFFICHAGE:
            input(f"\n[Tour Joueur {joueur_actuel+1}] Appuyez sur Entrée...")
        
        de = lancer_de()
        tours[joueur_actuel] += 1
        ancienne = joueurs[joueur_actuel]
        nouvelle = avancer(joueurs, joueur_actuel, de, stats)
        
        if MODE_AFFICHAGE:
            print(f"Dé : {de} | {ancienne} -> {nouvelle}")

        if nouvelle >= 100:
            return {"gagnant": joueur_actuel, "tours": tours, "stats": stats}
        
        joueur_actuel = (joueur_actuel + 1) % nb_joueurs
        if joueur_actuel == 0 and MODE_AFFICHAGE:
            afficher_plateau(joueurs)

def etude_statistique():
    global MODE_AFFICHAGE
    MODE_AFFICHAGE = False
    
    try:
        nb_parties = int(input("Nombre de parties à simuler : "))
        nb_joueurs = int(input("Nombre de joueurs (1-4) : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return

    victoires = [0] * nb_joueurs
    total_tours = [0] * nb_joueurs

    for i in range(nb_parties):
        res = jouer_une_partie(nb_joueurs)
        victoires[res["gagnant"]] += 1
        for j in range(nb_joueurs):
            total_tours[j] += res["tours"][j]
        
        if (i + 1) % 100 == 0:
            print(f"Simulation : {i + 1} parties terminées...")

    print("\n" + "="*30)
    print("RÉSULTATS DES SIMULATIONS")
    for j in range(nb_joueurs):
        print(f"\nJoueur {j+1}:")
        print(f" - Victoires : {victoires[j]} ({(victoires[j]/nb_parties)*100:.1f}%)")
        print(f" - Moyenne de tours : {total_tours[j]/nb_parties:.2f}")

def deroulement():
    global MODE_AFFICHAGE
    print("\n--- SERPENTS ET ÉCHELLES ---")
    print("1. Jouer une partie")
    print("2. Lancer une étude statistique")
    choix = input("Votre choix : ")

    if choix == "1":
        MODE_AFFICHAGE = True
        nb_j = int(input("Nombre de joueurs (1-4) : "))
        res = jouer_une_partie(nb_j)
        print(f"\nFÉLICITATIONS ! Le joueur {res['gagnant']+1} a gagné en {res['tours'][res['gagnant']]} tours !")
    elif choix == "2":
        etude_statistique()
    else:
        print("Choix invalide.")

if __name__ == "__main__":
    deroulement()