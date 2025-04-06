import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

# Fonction pour afficher une boîte de message
def afficher_message():
    messagebox.showinfo("Message", "Ceci est un message d'information!")

# Fonction pour changer le texte du label
def changer_texte_label():
    nouveau_texte = simpledialog.askstring("Entrée", "Entrez un nouveau texte pour le label:")
    if nouveau_texte:
        label_texte.config(text=nouveau_texte)

# Fonction pour ouvrir un fichier
def ouvrir_fichier():
    fichier = filedialog.askopenfilename(title="Ouvrir un fichier", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if fichier:
        with open(fichier, "r") as f:
            contenu = f.read()
        text_area.delete(1.0, tk.END)  # Efface le contenu actuel de la zone de texte
        text_area.insert(tk.END, contenu)  # Affiche le contenu du fichier dans la zone de texte

# Fonction pour sauvegarder le contenu de la zone de texte
def sauvegarder_fichier():
    fichier = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if fichier:
        with open(fichier, "w") as f:
            f.write(text_area.get(1.0, tk.END))  # Sauvegarde le texte de la zone de texte

# Fonction pour fermer l'application
def quitter():
    if messagebox.askyesno("Quitter", "Voulez-vous vraiment quitter ?"):
        root.quit()

# Fonction pour afficher une fenêtre "A propos"
def afficher_a_propos():
    messagebox.showinfo("À propos", "Application démonstration des fonctionnalités de Tkinter")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Démo Tkinter")
root.geometry("600x400")

# Créer une barre de menu
menu_bar = tk.Menu(root)

# Menu "Fichier"
menu_fichier = tk.Menu(menu_bar, tearoff=0)
menu_fichier.add_command(label="Ouvrir", command=ouvrir_fichier)
menu_fichier.add_command(label="Sauvegarder", command=sauvegarder_fichier)
menu_fichier.add_separator()
menu_fichier.add_command(label="Quitter", command=quitter)
menu_bar.add_cascade(label="Fichier", menu=menu_fichier)

# Menu "Aide"
menu_aide = tk.Menu(menu_bar, tearoff=0)
menu_aide.add_command(label="À propos", command=afficher_a_propos)
menu_bar.add_cascade(label="Aide", menu=menu_aide)

# Affichage de la barre de menu
root.config(menu=menu_bar)

# Créer un label dynamique
label_texte = tk.Label(root, text="Ceci est un label dynamique.", font=("Helvetica", 14))
label_texte.pack(pady=20)

# Créer un bouton pour changer le texte du label
button_changer_label = tk.Button(root, text="Changer le texte du label", command=changer_texte_label)
button_changer_label.pack(pady=10)

# Créer un bouton pour afficher un message
button_message = tk.Button(root, text="Afficher un message", command=afficher_message)
button_message.pack(pady=10)

# Créer une zone de texte
text_area = tk.Text(root, height=10, width=50)
text_area.pack(pady=20)

# Créer un bouton pour ouvrir un fichier
button_ouvrir_fichier = tk.Button(root, text="Ouvrir un fichier", command=ouvrir_fichier)
button_ouvrir_fichier.pack(pady=10)

# Créer un bouton pour sauvegarder un fichier
button_sauvegarder_fichier = tk.Button(root, text="Sauvegarder un fichier", command=sauvegarder_fichier)
button_sauvegarder_fichier.pack(pady=10)

# Ajouter un cadre pour organiser les boutons et autres widgets
frame = tk.Frame(root)
frame.pack(pady=20)

# Créer des boutons dans le cadre
button_1 = tk.Button(frame, text="Bouton 1", command=lambda: messagebox.showinfo("Action", "Bouton 1 cliqué"))
button_1.grid(row=0, column=0, padx=10)

button_2 = tk.Button(frame, text="Bouton 2", command=lambda: messagebox.showinfo("Action", "Bouton 2 cliqué"))
button_2.grid(row=0, column=1, padx=10)

button_3 = tk.Button(frame, text="Bouton 3", command=lambda: messagebox.showinfo("Action", "Bouton 3 cliqué"))
button_3.grid(row=0, column=2, padx=10)

# Lancer la boucle principale
root.mainloop()
