import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import os
import time


class NeoNetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NeoNet")
        self.root.geometry("600x500")
        self.root.configure(bg="#0E0E2A")
        self.pages_file = "sacos/pages.json"
        self.pages = self.load_pages()

        self.setup_ui()

    def setup_ui(self):
        title_frame = tk.Frame(self.root, bg="#4F6D7A", pady=20)
        title_frame.pack(fill="x")

        title_label = tk.Label(title_frame, text="NeoNet", font=("Helvetica", 30, "bold"), fg="#F8F8F8", bg="#4F6D7A")
        title_label.pack()

        self.search_frame = tk.Frame(self.root, bg="#0E0E2A")
        self.search_frame.pack(pady=20)

        self.search_entry = ttk.Entry(self.search_frame, width=40, font=("Helvetica", 12))
        self.search_entry.pack(padx=10, pady=10)

        self.search_button = ttk.Button(self.search_frame, text="Chercher", command=self.search_page, width=20, style="TButton")
        self.search_button.pack(pady=5)

        self.create_button = ttk.Button(self.root, text="Créer un site", command=self.open_create_site_window, width=20, style="TButton")
        self.create_button.pack(pady=10)

        self.results_frame = tk.Frame(self.root)
        self.results_frame.pack(pady=20, fill="both", expand=True)

        self.info_label = tk.Label(self.root, text="Entrez une recherche ci-dessus", font=("Helvetica", 12), fg="gray", bg="#0E0E2A")
        self.info_label.pack(pady=10)

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), foreground="white", background="#4F6D7A", padding=10)
        style.map("TButton", background=[("active", "#3D5563")])

    def load_pages(self):
        if os.path.exists(self.pages_file):
            with open(self.pages_file, "r") as file:
                return json.load(file)
        return []

    def save_pages(self):
        with open(self.pages_file, "w") as file:
            json.dump(self.pages, file, indent=4)

    def search_page(self):
        query = self.search_entry.get().lower()
        if not query:
            messagebox.showwarning("Erreur", "Veuillez entrer un mot-clé pour la recherche.")
            return

        results = [page for page in self.pages if any(keyword.lower() in query for keyword in page["keywords"])]

        for widget in self.results_frame.winfo_children():
            widget.destroy()

        if results:
            for page in results:
                button = ttk.Button(self.results_frame, text=page["name"], command=lambda p=page: self.open_page(p), width=40, style="TButton")
                button.pack(pady=5, fill="x")
        else:
            messagebox.showinfo("Résultats", "Aucun site trouvé pour cette recherche.")

    def open_create_site_window(self):
        create_window = tk.Toplevel(self.root)
        create_window.title("Créer un site")
        create_window.geometry("400x300")
        create_window.configure(bg="#0E0E2A")

        frame = tk.Frame(create_window, bg="#0E0E2A", padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Nom du site:", font=("Helvetica", 12), bg="#0E0E2A", fg="white").pack(pady=5)
        name_entry = ttk.Entry(frame, width=40)
        name_entry.pack(pady=5)

        tk.Label(frame, text="Texte du site:", font=("Helvetica", 12), bg="#0E0E2A", fg="white").pack(pady=5)
        text_entry = tk.Text(frame, width=40, height=5, font=("Helvetica", 12))
        text_entry.pack(pady=5)

        tk.Label(frame, text="Mots-clés (séparés par des ;):", font=("Helvetica", 12), bg="#0E0E2A", fg="white").pack(pady=5)
        keywords_entry = ttk.Entry(frame, width=40)
        keywords_entry.pack(pady=5)

        def save_site():
            name = name_entry.get()
            text = text_entry.get("1.0", tk.END).strip()
            keywords = [keyword.strip() for keyword in keywords_entry.get().split(";")]

            if not name or not text or not keywords:
                messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
                return

            if len(keywords) < 1:
                messagebox.showerror("Erreur", "Veuillez entrer au moins un mot-clé.")
                return

            self.pages.append({"name": name, "text": text, "keywords": keywords})
            self.save_pages()
            messagebox.showinfo("Succès", "Le site a été créé avec succès!")

            self.update_info_label("Site créé avec succès !")
            create_window.destroy()
            self.search_page()

        create_button = ttk.Button(frame, text="Sauvegarder", command=save_site, style="TButton")
        create_button.pack(pady=10)

    def open_page(self, page):
        page_window = tk.Toplevel(self.root)
        page_window.title(page["name"])
        page_window.geometry("400x300")
        page_window.configure(bg="#0E0E2A")

        text_widget = tk.Text(page_window, width=40, height=10, font=("Helvetica", 12), bg="#0E0E2A", fg="white")
        text_widget.insert(tk.END, page["text"])
        text_widget.pack(pady=20)

        scrollbar = tk.Scrollbar(page_window, command=text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_widget.config(yscrollcommand=scrollbar.set)

    def update_info_label(self, text):
        self.info_label.config(text=text)
        self.info_label.after(3000, lambda: self.info_label.config(text="Entrez une recherche ci-dessus"))

root = tk.Tk()
app = NeoNetApp(root)
root.mainloop()
