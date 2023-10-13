import tkinter as tk

root = tk.Tk()
root.minsize(200, 200)

btn_list = []

def affichage():
    """
    Affiche la grille
    Entrée : Aucune
    Sortie : Aucune
    """
    global btn_list
    for ligne in btn_list:
        for bouton in ligne:
            val = int(bouton['text'])
            if val == 0:
                couleur = '#000000'
                police = '#FFFFFF'
            elif val ==1:
                couleur='#404040'
                police='#BFBFBF'
            elif val ==2:
                couleur='#808080'
                police= '#FFFFFF'
            elif val ==3:
                couleur='#C1C1C1'
                police='#3E3E3E'
                
            else:
                couleur='#FFFFFF'
                police ='#000000'
            bouton['bg'] = couleur
            bouton['fg'] = police

def actualisation():
    """
    Actualise le plateau de jeu selon les règles définies
    Entrée : Aucune
    Sortie : Aucune
    """
    global btn_list 
    for ligne in range(len(btn_list)):
        for case in range(len(btn_list)):
            bouton=btn_list[ligne][case]
            val = int(bouton['text'])
            if val>=4:
                #Haut
                if ligne - 1 >=0:
                    btn_list[ligne-1][case]['text'] = int(btn_list[ligne-1][case]['text'] )+1
                #Bas
                if ligne + 1 <len(btn_list):
                    btn_list[ligne+1][case]['text'] = int(btn_list[ligne+1][case]['text'] )+1
                #Gauche
                if case - 1 >= 0:
                    btn_list[ligne][case-1]['text'] = int(btn_list[ligne][case-1]['text'] )+1
                #Droite
                if case + 1 < len(btn_list):
                    btn_list[ligne][case+1]['text'] = int(btn_list[ligne][case+1]['text'] )+1

                bouton['text'] = val-4

def onClick_validation(entree):
    """
    Gère les appuis sur le bouton de validation pour qu'il lance l'actualisation et rafraichisse la grille
    Entrée : entree (int, nombre d'actualisations à effectuer)
    Sortie : Aucune
    """
    repetitions=int(entree.get())

    for i in range(repetitions):
        actualisation()

    affichage()
    
def maj_bouton(param):
    """
    Mets à jour la valeur d'un tas de sable, symbolisé par un bouton
    Entrée : param (list, 0 -> tk.Button, le bouton à modifier
                          1 -> tk.Entry, l'objet où est entrée la nouvelle valeur du tas/bouton
                          2 -> tk.Tk, fenêtre de sélection de la valeur du tas de sable à fermer à la fin de la fonction)
    Sortie : Aucune
    """
    bouton = param[0]
    
    n_val = param[1].get()

    bouton['text']=n_val
    param[2].destroy()
    affichage()

def onClick_bouton(idx):
    """
    Gère les appuis sur les boutons/tas
    Entrée : idx (tuple, coordonnées du bouton servant à l'identifier)
    Sortie : Aucune
    """
    i,j=idx
    bouton = btn_list[i][j]
    
    fen_choix_nb=tk.Tk()
    label_choix_nb=tk.Label(fen_choix_nb, text="Combien de grains sur cette case ?")
    entry_choix_nb=tk.Entry(fen_choix_nb)
    validation_choix_nb=tk.Button(fen_choix_nb, text='Valider', command=lambda param = (bouton,entry_choix_nb,fen_choix_nb) : maj_bouton (param))

    label_choix_nb.grid(row = 0, column = 0)
    entry_choix_nb.grid(row = 0, column = 1)
    validation_choix_nb.grid(row = 0, column = 2)

    entry_choix_nb.focus_set()


    
    
#Génération des boutons/tas de sable (grille de 21x21)
for i in range(21):
    btn_list.append([])
    for j in range(21):
        b = tk.Button(root, text = 3, command = lambda idx = (i,j) : onClick_bouton(idx), width=2, height=1)
        b.grid(row = i, column = j)

        btn_list[i].append(b)

#Génération de la fenêtre et des différents objest à afficher
label0_validation = tk.Label(root,text='Actualiser ')
entry_validation  = tk.Entry(root)
label1_validation = tk.Label(root,text=' fois')
validation = tk.Button(root,text='Valider',command= lambda entree = entry_validation : onClick_validation(entree))

#Affichage initial de la fenêtre
label0_validation.place(anchor=tk.SW,x=0,y=700)
entry_validation.place(anchor=tk.SW,x=80,y=700)
label1_validation.place(anchor=tk.SW,x=250,y=700)
validation.place(anchor=tk.SW,x=300,y=700)
root.mainloop()
