import tkinter as tk
from tkinter import messagebox
import json
import os

def charger_utilisateurs():
    if os.path.exists('sacos/users.json'):
        with open('sacos/users.json', 'r') as f:
            return json.load(f)
    return {}

def sauvegarder_utilisateurs(utilisateurs):
    with open('sacos/users.json', 'w') as f:
        json.dump(utilisateurs, f)

def verifier_connexion():
    identifiant = entry_identifiant.get()
    mot_de_passe = entry_mot_de_passe.get()
    utilisateurs = charger_utilisateurs()
    if identifiant in utilisateurs and utilisateurs[identifiant] == mot_de_passe:
        messagebox.showinfo("Bienvenue", f"Bienvenue, {identifiant}!")
        import sacos.bp as bp
    else:
        messagebox.showerror("Erreur", "Identifiant ou mot de passe incorrect.")

def ouvrir_page_principale():
    connexion_window.destroy()
    import sacos.bp as bp

def ouvrir_creation_compte():
    creation_window = tk.Toplevel(connexion_window)
    creation_window.title("Créer un compte")
    creation_window.geometry("400x300")
    label_titre_creation = tk.Label(creation_window, text="Créer un compte", font=("Helvetica", 18))
    label_titre_creation.pack(pady=20)
    label_identifiant_creation = tk.Label(creation_window, text="Identifiant:")
    label_identifiant_creation.pack(pady=5)
    entry_identifiant_creation = tk.Entry(creation_window)
    entry_identifiant_creation.pack(pady=5)
    label_mot_de_passe_creation = tk.Label(creation_window, text="Mot de passe:")
    label_mot_de_passe_creation.pack(pady=5)
    entry_mot_de_passe_creation = tk.Entry(creation_window, show="*")
    entry_mot_de_passe_creation.pack(pady=5)

    def creer_compte():
        identifiant = entry_identifiant_creation.get()
        mot_de_passe = entry_mot_de_passe_creation.get()
        utilisateurs = charger_utilisateurs()
        if identifiant in utilisateurs:
            messagebox.showerror("Erreur", "Cet identifiant est déjà pris.")
        else:
            utilisateurs[identifiant] = mot_de_passe
            sauvegarder_utilisateurs(utilisateurs)
            messagebox.showinfo("Succès", "Compte créé avec succès!")
            creation_window.destroy()

    button_creation = tk.Button(creation_window, text="Créer le compte", command=creer_compte)
    button_creation.pack(pady=20)

connexion_window = tk.Tk()
connexion_window.title("Écran de Connexion")
connexion_window.geometry("400x300")
label_titre = tk.Label(connexion_window, text="Se connecter", font=("Helvetica", 18))
label_titre.pack(pady=20)
label_identifiant = tk.Label(connexion_window, text="Identifiant:")
label_identifiant.pack(pady=5)
entry_identifiant = tk.Entry(connexion_window)
entry_identifiant.pack(pady=5)
label_mot_de_passe = tk.Label(connexion_window, text="Mot de passe:")
label_mot_de_passe.pack(pady=5)
entry_mot_de_passe = tk.Entry(connexion_window, show="*")
entry_mot_de_passe.pack(pady=5)
button_connexion = tk.Button(connexion_window, text="Se connecter", command=verifier_connexion)
button_connexion.pack(pady=10)
button_creation_compte = tk.Button(connexion_window, text="Créer un nouveau compte", command=ouvrir_creation_compte)
button_creation_compte.pack(pady=10)
connexion_window.mainloop()
