import tkinter as tk
import random
import string

RULES = [
    "Règle 1 : Votre mot de passe doit contenir au moins 5 caractères.",
    "Règle 2 : Votre mot de passe doit inclure un chiffre.",
    "Règle 3 : Votre mot de passe doit inclure une lettre majuscule.",
    "Règle 4 : Votre mot de passe doit inclure un caractère spécial (par exemple, !, @, #, etc.).",
    "Règle 5 : Les chiffres de votre mot de passe doivent additionner à 25.",
    "Règle 6 : Votre mot de passe doit inclure un mois de l'année (ex : janvier, février, etc.).",
    "Règle 7 : Votre mot de passe doit inclure un chiffre romain.",
    "Règle 8 : Les chiffres romains dans votre mot de passe doivent multiplier pour donner 35.",
    "Règle 9 : Votre mot de passe ne doit pas contenir des mots complets du dictionnaire.",
    "Règle 10 : Votre mot de passe ne doit pas inclure votre nom ou prénom.",
    "Règle 11 : Votre mot de passe ne doit pas commencer par un chiffre.",
    "Règle 12 : Votre mot de passe ne doit pas contenir de répétitions comme 'aaaa' ou '1111'.",
    "Règle 13 : Les lettres de votre mot de passe doivent alterner entre majuscule et minuscule.",
    "Règle 14 : Il ne doit pas y avoir d'espaces dans votre mot de passe.",
    "Règle 15 : Votre mot de passe ne doit pas inclure des séquences simples comme '1234' ou 'abcd'.",
    "Règle 16 : Votre mot de passe doit inclure au moins une lettre accentuée (é, è, à, etc.).",
    "Règle 17 : Votre mot de passe ne doit pas commencer ou finir par un caractère spécial.",
    "Règle 18 : Votre mot de passe doit contenir au moins une voyelle et une consonne.",
    "Règle 19 : Votre mot de passe ne doit pas contenir plus de trois chiffres consécutifs.",
    "Règle 20 : Votre mot de passe ne doit pas être identique à votre adresse e-mail.",
    "Règle 21 : Votre mot de passe doit contenir une combinaison de 3 ou plus de caractères répétés dans un ordre inversé (ex : 'abc' et 'cba').",
    "Règle 22 : Votre mot de passe doit contenir exactement 2 majuscules et 2 minuscules.",
    "Règle 23 : Votre mot de passe ne doit pas inclure des dates ou années évidentes."
]

months = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def generate_password():
    length = random.randint(5, 12)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    while not (any(c.islower() for c in password) and
               any(c.isupper() for c in password) and
               any(c.isdigit() for c in password) and
               any(c in string.punctuation for c in password)):
        password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def validate_password(password, username):
    if len(password) < 5:
        return "Le mot de passe doit contenir au moins 5 caractères."

    if not any(c.isdigit() for c in password):
        return "Votre mot de passe doit inclure un chiffre."

    if not any(c.isupper() for c in password):
        return "Votre mot de passe doit inclure une lettre majuscule."

    if not any(c in string.punctuation for c in password):
        return "Votre mot de passe doit inclure un caractère spécial."

    digits = [int(c) for c in password if c.isdigit()]
    if sum(digits) != 25:
        return "Les chiffres de votre mot de passe doivent additionner à 25."

    if not any(month in password for month in months):
        return "Votre mot de passe doit inclure un mois de l'année."

    if not any(roman in password for roman in roman_numerals):
        return "Votre mot de passe doit inclure un chiffre romain."

    roman_chars = [c for c in password if c in roman_numerals]
    roman_values = [roman_numerals[c] for c in roman_chars]
    if roman_values and (len(roman_values) > 1 and (roman_values[0] * roman_values[1]) != 35):
        return "Les chiffres romains dans votre mot de passe doivent multiplier pour donner 35."

    common_words = ['password', '1234', 'abcd', 'qwerty']
    if any(word in password.lower() for word in common_words):
        return "Votre mot de passe ne doit pas contenir des mots du dictionnaire."

    if username.lower() in password.lower():
        return "Votre mot de passe ne doit pas inclure votre nom ou prénom."

    if password[0].isdigit():
        return "Votre mot de passe ne doit pas commencer par un chiffre."

    if any(password[i:i+4] == password[i]*4 for i in range(len(password)-3)):
        return "Votre mot de passe ne doit pas contenir de répétitions comme 'aaaa' ou '1111'."

    if not all((password[i].isupper() if i % 2 == 0 else password[i].islower()) for i in range(len(password))):
        return "Les lettres de votre mot de passe doivent alterner entre majuscule et minuscule."

    if ' ' in password:
        return "Il ne doit pas y avoir d'espaces dans votre mot de passe."

    if any(seq in password for seq in ['1234', 'abcd', 'qwerty']):
        return "Votre mot de passe ne doit pas inclure des séquences simples comme '1234' ou 'abcd'."

    if not any(c in "éèà" for c in password):
        return "Votre mot de passe doit inclure au moins une lettre accentuée (é, è, à, etc.)."

    if password[0] in string.punctuation or password[-1] in string.punctuation:
        return "Votre mot de passe ne doit pas commencer ou finir par un caractère spécial."

    if not any(c in "aeiou" for c in password) or not any(c not in "aeiou" for c in password):
        return "Votre mot de passe doit contenir au moins une voyelle et une consonne."

    if any(password[i:i+3].isdigit() for i in range(len(password)-2)):
        return "Votre mot de passe ne doit pas contenir plus de trois chiffres consécutifs."

    if username.lower() in password.lower():
        return "Votre mot de passe ne doit pas être identique à votre adresse e-mail."

    if not any(password[i:i+3] == password[i+3:i+6][::-1] for i in range(len(password)-5)):
        return "Votre mot de passe doit contenir une combinaison de 3 ou plus de caractères répétés dans un ordre inversé."

    if password.count("A") != 2 or password.count("a") != 2:
        return "Votre mot de passe doit contenir exactement 2 majuscules et 2 minuscules."

    if any(year in password for year in ["2023", "2024", "2025"]):
        return "Votre mot de passe ne doit pas inclure des dates ou années évidentes."

    return "Mot de passe valide !"

class PasswordGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu du Mot de Passe")
        
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.show_password = False
        self.rule_index = 0
        
        self.create_widgets()
        self.show_rules()

    def create_widgets(self):
        tk.Label(self.root, text="Entrez votre nom d'utilisateur :").pack()
        self.username_entry = tk.Entry(self.root, textvariable=self.username)
        self.username_entry.pack()
        
        tk.Label(self.root, text="Entrez votre mot de passe :").pack()
        self.password_entry = tk.Entry(self.root, textvariable=self.password, show="*")
        self.password_entry.pack()
        
        self.submit_button = tk.Button(self.root, text="Valider", command=self.validate)
        self.submit_button.pack()
        
        self.toggle_button = tk.Button(self.root, text="Afficher/Masquer le mot de passe", command=self.toggle_password)
        self.toggle_button.pack()

        self.rules_label = tk.Label(self.root, text="", justify="left")
        self.rules_label.pack()
        
        self.result_label = tk.Label(self.root, text="", fg="red")
        self.result_label.pack()

    def show_rules(self):
        if self.rule_index < len(RULES):
            rule = RULES[self.rule_index]
            current_text = self.rules_label.cget("text")
            self.rules_label.config(text=current_text + "\n" + rule)
            self.rule_index += 1
            self.root.after(1000, self.show_rules)  # Afficher la règle suivante après 1 seconde

    def validate(self):
        username = self.username.get()
        password = self.password.get()
        
        validation_result = validate_password(password, username)
        self.result_label.config(text=validation_result)
        
    def toggle_password(self):
        if self.show_password:
            self.password_entry.config(show="*")
            self.toggle_button.config(text="Afficher/Masquer le mot de passe")
        else:
            self.password_entry.config(show="")
            self.toggle_button.config(text="Masquer le mot de passe")
        self.show_password = not self.show_password
        

root = tk.Tk()
game = PasswordGame(root)
root.mainloop()
