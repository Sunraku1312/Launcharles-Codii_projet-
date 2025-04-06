import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import json

try:
    with open("sacos/bot_responses.json", "r") as f:
        bot_data = json.load(f)
except FileNotFoundError:
    bot_data = {}

def get_bot_response(event=None): 
    user_input = user_entry.get().strip().lower()
    
    if user_input == "quitter":
        root.quit()
        return
    
    if user_input in bot_data:
        bot_response = bot_data[user_input]
    else:
        bot_response = "Je ne sais pas quoi répondre."
        new_response = simpledialog.askstring("Nouvelle Réponse", f"Que dois-je répondre à '{user_input}' ?")
        if new_response:
            bot_data[user_input] = new_response
            with open("bot_responses.json", "w") as f:
                json.dump(bot_data, f, indent=4)
            bot_response = f"Merci ! Je vais m'en souvenir pour la prochaine fois."
    
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"Tu: {user_input}\n")
    chat_box.insert(tk.END, f"Bot: {bot_response}\n\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)
    
    user_entry.delete(0, tk.END)

def quit_app():
    root.quit()

def open_json_editor():
    def save_changes():
        try:
            modified_data = json.loads(json_text.get("1.0", tk.END))
            with open("bot_responses.json", "w") as f:
                json.dump(modified_data, f, indent=4)
            messagebox.showinfo("Succès", "Les réponses ont été mises à jour avec succès.")
            editor_window.destroy()
        except json.JSONDecodeError:
            messagebox.showerror("Erreur", "Le format JSON est invalide. Veuillez vérifier les données.")
    
    editor_window = tk.Toplevel(root)
    editor_window.title("Éditeur de Réponses Bot")
    editor_window.geometry("600x400")
    
    frame = tk.Frame(editor_window)
    frame.pack(fill=tk.BOTH, expand=True)

    json_text = tk.Text(frame, height=15, width=70)
    json_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    v_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=json_text.yview)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    h_scrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL, command=json_text.xview)
    h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    json_text.config(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    json_text.insert(tk.END, json.dumps(bot_data, indent=4))
    
    save_button = tk.Button(editor_window, text="Enregistrer les modifications", command=save_changes)
    save_button.pack(pady=5)

root = tk.Tk()
root.title("Chat avec le Bot")

# Créer un frame pour la zone de texte du chat et la scrollbar
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

chat_box = tk.Text(frame, height=20, width=50, state=tk.DISABLED, wrap=tk.WORD)
chat_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Barre de défilement verticale pour le chat
v_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=chat_box.yview)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_box.config(yscrollcommand=v_scrollbar.set)

user_entry = tk.Entry(root, width=40)
user_entry.pack(padx=10, pady=10)

send_button = tk.Button(root, text="Envoyer", command=get_bot_response)
send_button.pack(pady=5)

quit_button = tk.Button(root, text="Quitter", command=quit_app)
quit_button.pack(pady=5)

edit_button = tk.Button(root, text="Modifier Réponses", command=open_json_editor)
edit_button.pack(pady=5)

user_entry.bind("<Return>", get_bot_response)

root.mainloop()