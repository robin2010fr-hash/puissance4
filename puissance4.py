def creer_plateau():
    plateau = [["_" for _ in range(7)] for _ in range(6)]
    return plateau

def affichage_plateau(tab):
    # On ajuste le nombre d'espaces au-dessus pour aligner avec les symboles
    print("  1  2  3  4  5  6  7")
    texte_ligne = "|"
    for l in range(len(tab)):
        for c in range(len(tab[0])):
            texte_ligne += f" {tab[l][c]} |"
        print(f"{texte_ligne}")
        texte_ligne = "|"

def colonne_valide(tab,c):
    if c < 0 or c > 6:
        return False
    else:
        return tab[0][c] == '_'

def coup_est_valide(tab,c,symbole):
    if colonne_valide(tab,c) == False:
        return False, tab
    else:
        for j in range(len(tab)):
            i = -(j+1)
            if tab[i][c] == '_':
                tab[i][c] = symbole
                return True, tab

def victoire_horizontale(tab, sym):
    for l in range(6):
        for c in range(4):
            if tab[l][c] == tab[l][c+1] == tab[l][c+2] == tab[l][c+3] == sym:
                return True
    return False

def victoire_verticale(tab, sym):
    for c in range(7):
        for l in range(3):
            if tab[l][c] == tab[l+1][c] == tab[l+2][c] == tab[l+3][c] == sym:
                return True
    return False

def victoire_diagonale_descendante(tab, sym):
    for l in range(3):
        for c in range(4):
            if tab[l][c] == tab[l+1][c+1] == tab[l+2][c+2] == tab[l+3][c+3] == sym:
                return True
    return False

def victoire_diagonale_montante(tab, sym):
    for l in range(3, 6):
        for c in range(4):
            if tab[l][c] == tab[l-1][c+1] == tab[l-2][c+2] == tab[l-3][c+3] == sym:
                return True
    return False

def victoire(tab, sym):
    return (victoire_horizontale(tab, sym) or
            victoire_verticale(tab, sym) or
            victoire_diagonale_descendante(tab, sym) or
            victoire_diagonale_montante(tab, sym))

def jeu_J1_J2(plateau,joueur,symbole,n1,n2):
    valide = False
    nom_actuel = n1 if joueur == 1 else n2
    affichage_plateau(plateau)
    print()
    colonne_choisi = int(input(f"Quelle colonne choisis-tu ? ({nom_actuel} - {symbole}) "))
    colonne_choisi -= 1
    valide, plateau = coup_est_valide(plateau,colonne_choisi,symbole)
    while valide == False:
        print()
        colonne_choisi = int(input(f"Erreur. Mauvaise colonne. Ressaie. ({nom_actuel} - {symbole}) "))
        colonne_choisi -= 1
        valide, plateau  = coup_est_valide(plateau,colonne_choisi,symbole)
    return plateau

def jouer_partie(plateau,nom_j1,nom_j2):
    symbole = ""
    win = False
    full_plateau = False
    joueur = 0
    voy_j1 = nom_j1[0].upper() in ["A", "E", "I", "O", "U", "Y"]
    voy_j2 = nom_j2[0].upper() in ["A", "E", "I", "O", "U", "Y"]
    
    
    while win == False and full_plateau == False:    
        for joueur in range(1, 3):
            if joueur == 1:
                symbole = "X"
            else:
                symbole = "O"
                
            plateau = jeu_J1_J2(plateau, joueur, symbole, nom_j1, nom_j2)
            
            if victoire(plateau, symbole) == True:
                win = True
                break
                
        # Vérification si la grille est pleine (sur les 7 colonnes)
        if all(plateau[0][c] != "_" for c in range(7)):
            full_plateau = True
            break
            
    print()
    affichage_plateau(plateau)
    print()
    
    if win == True:
        if joueur == 1:
            if voy_j1 == True:
                print(f"Victoire d'{nom_j1} (symbole :{symbole}!")
            else:
                print(f"Victoire de {nom_j1} (symbole :{symbole}!")
        elif joueur == 2:
            if voy_j2 == True:
                print(f"Victoire d'{nom_j2} (symbole :{symbole}!")
            else:
                print(f"Victoire de {nom_j2} (symbole :{symbole}!")
            
    elif full_plateau == True:
        print("Match nul, personne n'a gagné...")


def jeu():
    input("Appuie sur Entrée pour défiler le texte")
    input("""
Tu vas jouer au Puissance 4""")
    choix = input("""
Veux-tu que je t'explique les règles (o/n)""")
    if choix == "o":
        input("""
Règles : Aligner 4 pions horizontalement, verticalement ou en diagonale...""")
        input("... avant que ton adversiare le fasse avant toi!")
    new_game = True
    while new_game == True:
        input("""
Place au jeu""")
        name_j1 = input("Qui commence ? (ex : \033[1mT\033[0miteuf)")
        name_j2 = input("Et qui prends la relève ? (ex : \033[1mT\033[0mitof)")
        jouer_partie(creer_plateau(),name_j1,name_j2)
        print()
        rejouer = input("""
Voulez-vous rejouer ? (o/n)""")
        if rejouer == "n":
            new_game = False
    print()
    print("""
A plus tard""")

jeu()
