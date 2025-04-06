import tkinter as tk
from tkinter import messagebox
import random
import string
import json
from cryptography.fernet import Fernet
import base64
import pyperclip

def generer_cle():
    return Fernet.generate_key()

def charger_cle():
    try:
        with open("sacos/cle_secrete.key", "rb") as cle_file:
            cle = cle_file.read()
    except FileNotFoundError:
        cle = generer_cle()
        with open("sacos/cle_secrete.key", "wb") as cle_file:
            cle_file.write(cle)
    return cle

def crypter_mot_de_passe(mot_de_passe, cle):
    cipher_suite = Fernet(cle)
    mot_de_passe_crypte = cipher_suite.encrypt(mot_de_passe.encode())
    return mot_de_passe_crypte

def decrypter_mot_de_passe(mot_de_passe_crypte, cle):
    cipher_suite = Fernet(cle)
    mot_de_passe = cipher_suite.decrypt(mot_de_passe_crypte).decode()
    return mot_de_passe

def generer_mot_de_passe(longueur=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longueur))

def encoder_base64(data):
    return base64.b64encode(data).decode('utf-8')

def decoder_base64(data):
    return base64.b64decode(data.encode('utf-8'))

def enregistrer_mot_de_passe(nom, mot_de_passe, cle):
    try:
        with open("sacos/mots_de_passe.json", "r") as f:
            mots_de_passe = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        mots_de_passe = {}

    mot_de_passe_crypte = crypter_mot_de_passe(mot_de_passe, cle)
    mot_de_passe_base64 = encoder_base64(mot_de_passe_crypte)
    mots_de_passe[nom] = mot_de_passe_base64

    with open("sacos/mots_de_passe.json", "w") as f:
        json.dump(mots_de_passe, f, indent=4)

def recuperer_mot_de_passe(nom, cle):
    try:
        with open("sacos/mots_de_passe.json", "r") as f:
            mots_de_passe = json.load(f)
        mot_de_passe_base64 = mots_de_passe.get(nom, None)
        if mot_de_passe_base64:
            mot_de_passe_crypte = decoder_base64(mot_de_passe_base64)
            return decrypter_mot_de_passe(mot_de_passe_crypte, cle)
        return None
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def generer_et_enregistrer():
    nom = entry_nom.get()
    if not nom:
        messagebox.showerror("Erreur", "Veuillez entrer un nom pour le mot de passe.")
        return

    mot_de_passe = generer_mot_de_passe()
    cle = charger_cle()
    enregistrer_mot_de_passe(nom, mot_de_passe, cle)
    messagebox.showinfo("Succès", f"Mot de passe généré et enregistré pour '{nom}' :\n{mot_de_passe}")

def recuperer_mot_de_passe_par_nom():
    nom = entry_nom_recup.get()
    if not nom:
        messagebox.showerror("Erreur", "Veuillez entrer un nom pour récupérer le mot de passe.")
        return

    cle = charger_cle()
    mot_de_passe = recuperer_mot_de_passe(nom, cle)
    if mot_de_passe:
        messagebox.showinfo("Mot de passe", f"Le mot de passe pour '{nom}' est : {mot_de_passe}")
        label_mot_de_passe.config(text=f"Le mot de passe pour '{nom}' est : {mot_de_passe}")
    else:
        messagebox.showerror("Erreur", f"Aucun mot de passe trouvé pour '{nom}'.")

def copier_mot_de_passe():
    mot_de_passe = label_mot_de_passe.cget("text")
    if mot_de_passe:
        pyperclip.copy(mot_de_passe.split(": ")[1])
        messagebox.showinfo("Copié", "Mot de passe copié dans le presse-papiers.")
    else:
        messagebox.showerror("Erreur", "Aucun mot de passe à copier.")

def interface():
    global entry_nom, entry_nom_recup, label_mot_de_passe
    root = tk.Tk()
    root.title("Gestionnaire de mots de passe")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    label_nom = tk.Label(frame, text="Nom pour le mot de passe:")
    label_nom.grid(row=0, column=0, sticky="w", pady=5)

    entry_nom = tk.Entry(frame, width=30)
    entry_nom.grid(row=0, column=1, pady=5)

    bouton_generer = tk.Button(frame, text="Générer et enregistrer", command=generer_et_enregistrer)
    bouton_generer.grid(row=1, columnspan=2, pady=10)

    label_nom_recup = tk.Label(frame, text="Nom du mot de passe à récupérer:")
    label_nom_recup.grid(row=2, column=0, sticky="w", pady=5)

    entry_nom_recup = tk.Entry(frame, width=30)
    entry_nom_recup.grid(row=2, column=1, pady=5)

    bouton_recuperer = tk.Button(frame, text="Récupérer", command=recuperer_mot_de_passe_par_nom)
    bouton_recuperer.grid(row=3, columnspan=2, pady=10)

    label_mot_de_passe = tk.Label(frame, text="", width=40, anchor="w")
    label_mot_de_passe.grid(row=4, columnspan=2, pady=5)

    bouton_copier = tk.Button(frame, text="Copier", command=copier_mot_de_passe)
    bouton_copier.grid(row=5, columnspan=2, pady=10)

    root.mainloop()

interface()