import tkinter as tk

def SC ():
    import IDESC
    windowse.quit()

def rd ():
    import randome
    windowse.quit()

def sc ():
    import speakcactus
    windowse.quit()

def Nn ():
    import internet


windowse = tk.Tk()
windowse.title("SAC.OS")
windowse.geometry("600x400")

label_texte = tk.Label(windowse, text="SAC.OS", font=("Helvetica", 20))
label_texte.pack(pady=20)

button = tk.Button(windowse, text="IDE SC", command=SC)
button.pack(pady=20)

button2 = tk.Button(windowse, text="Chiffre alleatoire", command=rd)
button2.pack(pady=10)

button2 = tk.Button(windowse, text="speak cactus", command=sc)
button2.pack(pady=10)

button3 = tk.Button(windowse, text="NeoNet", command=Nn)
button3.pack(pady=10)

windowse.mainloop()