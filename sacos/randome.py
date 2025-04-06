import tkinter as tk
import time

root = tk.Tk()
root.title("Générateur de Nombre vraiment Aléatoire")

def generate_random_number():
    current_time = int(time.time() * 1000)
    random_number = (current_time * 16807) % 2147483647
    random_number = random_number % 100000
    random_label.config(text=f"Nombre aléatoire: {random_number}")

generate_button = tk.Button(root, text="Générer un Nombre", command=generate_random_number)
generate_button.pack(pady=20)

random_label = tk.Label(root, text="Nombre aléatoire: ", font=('Helvetica', 16))
random_label.pack(pady=20)

root.mainloop()