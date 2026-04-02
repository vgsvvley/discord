import turtle
import random

# --- CONFIGURATION ---
SERPENTS = {14: 4, 28: 10, 43: 1, 47: 18, 51: 31, 68: 33, 63: 39, 77: 26, 83: 58, 95: 53, 90: 70, 99: 80}
ECHELLES = {2: 20, 8: 30, 16: 37, 27: 69, 41: 62, 73: 94, 65: 79}
COULEURS = ["red", "blue", "green", "purple"]
TAILLE_CASE = 50

# --- LOGIQUE GRAPHIQUE ---
def obtenir_coordonnees(case):
    """Convertit un numéro de case (1-100) en coordonnées X, Y pour Turtle."""
    if case == 0: return (-225, -225) # Position de départ hors plateau
    
    case -= 1 # On passe en index 0-99
    ligne = case // 10
    colonne = case % 10
    
    # Inversion de direction une ligne sur deux (boustrophédon)
    if ligne % 2 == 1:
        colonne = 9 - colonne
        
    x = colonne * TAILLE_CASE - 225
    y = ligne * TAILLE_CASE - 225
    return (x, y)

def dessiner_plateau():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    for i in range(1, 101):
        x, y = obtenir_coordonnees(i)
        t.goto(x - TAILLE_CASE/2, y - TAILLE_CASE/2)
        t.pendown()
        for _ in range(4):
            t.forward(TAILLE_CASE)
            t.left(90)
        t.penup()
        t.goto(x, y - 10)
        t.write(str(i), align="center", font=("Arial", 10, "normal"))
    t.hideturtle()

# --- LOGIQUE DU JEU ---
def avancer(positions, joueur_actuel, valeur_de, pions):
    ancienne_pos = positions[joueur_actuel]
    nouvelle_pos = ancienne_pos + valeur_de
    
    print(f"Joueur {joueur_actuel+1} lance un {valeur_de}")

    # Gestion dépassement 100
    if nouvelle_pos > 100:
        reculement = nouvelle_pos - 100
        nouvelle_pos = 100 - reculement
        print(f"Trop loin ! On recule à la case {nouvelle_pos}")

    # Serpents et Échelles
    if nouvelle_pos in SERPENTS:
        print("OH NON ! Un serpent !")
        nouvelle_pos = SERPENTS[nouvelle_pos]
    elif nouvelle_pos in ECHELLES:
        print("SUPER ! Une échelle !")
        nouvelle_pos = ECHELLES[nouvelle_pos]

    positions[joueur_actuel] = nouvelle_pos
    
    # Animation du pion
    x, y = obtenir_coordonnees(nouvelle_pos)
    pions[joueur_actuel].goto(x, y)
    
    return nouvelle_pos

def jouer_turtle():
    # Setup Fenêtre
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title("Serpents et Échelles - Python Turtle")
    screen.tracer(0) # Désactive l'animation pendant le dessin du plateau
    
    dessiner_plateau()
    
    nb_joueurs = int(screen.numinput("Joueurs", "Combien de joueurs (1-4) ?", 2, minval=1, maxval=4))
    
    # Création des pions
    positions = [0] * nb_joueurs
    pions = []
    for i in range(nb_joueurs):
        p = turtle.Turtle()
        p.shape("circle")
        p.color(COULEURS[i])
        p.penup()
        p.goto(obtenir_coordonnees(0))
        pions.append(p)
    
    screen.tracer(1) # Réactive l'animation
    
    joueur_actuel = 0
    while True:
        # On attend un clic ou une touche pour lancer le dé
        msg = f"Joueur {joueur_actuel+1} (Cliquer OK pour lancer le dé)"
        screen.textinput("Tour suivant", msg)
        
        de = random.randint(1, 6)
        nouvelle = avancer(positions, joueur_actuel, de, pions)
        
        if nouvelle >= 100:
            print(f"VICTOIRE ! Le joueur {joueur_actuel+1} a gagné !")
            turtle.done()
            break
            
        joueur_actuel = (joueur_actuel + 1) % nb_joueurs

if __name__ == "__main__":
    jouer_turtle()