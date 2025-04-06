import tkinter as tk
import webbrowser

def ouvrir_site(url):
    """Ouvre le site web donné dans le navigateur par défaut."""
    webbrowser.open(url)

def rechercher_site():
    """Lance la recherche sur Google avec le texte entré dans la barre de recherche."""
    query = entry_recherche.get()  # Récupère le texte de la barre de recherche
    if query:
        url = f"https://www.google.com/search?q={query}"  # URL de recherche Google
        ouvrir_site(url)

root = tk.Tk()
root.title("Navigation vers les sites")

root.geometry("500x800")

label = tk.Label(root, text="Cliquez sur un bouton pour accéder au site", font=("Arial", 14))
label.pack(pady=20)

# Barre de recherche
label_recherche = tk.Label(root, text="Recherche Google:", font=("Arial", 10))
label_recherche.pack(pady=10)

entry_recherche = tk.Entry(root, width=40, font=("Arial", 12))
entry_recherche.pack(pady=5)

button_rechercher = tk.Button(root, text="Rechercher", width=30, height=2, command=rechercher_site)
button_rechercher.pack(pady=10)

# Boutons pour les sites spécifiques
button_chatgpt = tk.Button(root, text="ChatGPT", width=30, height=2, command=lambda: ouvrir_site("https://chat.openai.com"))
button_chatgpt.pack(pady=10)

button_google = tk.Button(root, text="Le Bon Coin", width=30, height=2, command=lambda: ouvrir_site("https://www.leboncoin.fr"))
button_google.pack(pady=10)

button_youtube = tk.Button(root, text="YouTube", width=30, height=2, command=lambda: ouvrir_site("https://www.youtube.com"))
button_youtube.pack(pady=10)

button_github = tk.Button(root, text="GitHub", width=30, height=2, command=lambda: ouvrir_site("https://www.github.com"))
button_github.pack(pady=10)

button_reddit = tk.Button(root, text="Reddit", width=30, height=2, command=lambda: ouvrir_site("https://www.reddit.com"))
button_reddit.pack(pady=10)

button_itcheio = tk.Button(root, text="itch.io", width=30, height=2, command=lambda: ouvrir_site("https://itch.io"))
button_itcheio.pack(pady=10)

button_parisien = tk.Button(root, text="Le Parisien", width=30, height=2, command=lambda: ouvrir_site("https://www.leparisien.fr"))
button_parisien.pack(pady=10)

button_amazon = tk.Button(root, text="Amazon", width=30, height=2, command=lambda: ouvrir_site("https://www.amazon.com"))
button_amazon.pack(pady=10)

button_wikipedia = tk.Button(root, text="Wikipedia", width=30, height=2, command=lambda: ouvrir_site("https://www.wikipedia.org"))
button_wikipedia.pack(pady=10)

root.mainloop()
