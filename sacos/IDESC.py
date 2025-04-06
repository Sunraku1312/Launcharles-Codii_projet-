import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog

def create_input_window(var_name, prompt, title):
    # Créer la fenêtre tkinter
    inputk = tk.Tk()
    inputk.title(title)
    inputk.geometry("300x150")  # Taille de la fenêtre

    # Créer un label pour afficher le prompt
    label = tk.Label(inputk, text=prompt)
    label.pack(pady=10)

    # Créer un champ de texte pour entrer la valeur
    entry = tk.Entry(inputk)
    entry.pack(pady=5)

    # Variable pour stocker la valeur entrée par l'utilisateur
    result = None
    def on_submite():
        nonlocal result
        result = entry.get()
        inputk.quit()

    # Créer un bouton pour valider l'entrée
    button = tk.Button(inputk, text="Entrer", command=on_submite)
    button.pack(pady=10)

    # Exécuter la fenêtre tkinter
    inputk.mainloop()

    return result


def interpreter_sc(code):
    variables = {}

    try:
        lines = code.splitlines()
        output = []

        for line in lines:
            line = line.strip()

            if line.startswith("print"):
                message = line[len("print "):].strip()
                # Si le message est une variable, on affiche la valeur
                if message in variables:
                    var_type, var_value = variables[message]
                    if var_type == "bin":
                        # Afficher la valeur binaire en chaîne
                        output.append(f"{bin(var_value)}")
                    else:
                        output.append(f"{var_value}")
                else:
                    output.append(f"Erreur: Variable '{message}' non définie")

            elif line.startswith("set"):
                parts = line[len("set "):].strip().split()
                if len(parts) == 3:
                    var_name = parts[0]
                    var_type = parts[1]
                    var_value = parts[2]

                    if var_type == "int":
                        try:
                            var_value = int(var_value)
                        except ValueError:
                            output.append(f"Erreur: Impossible de convertir '{var_value}' en entier")
                            continue
                    elif var_type == "float":
                        try:
                            var_value = float(var_value)
                        except ValueError:
                            output.append(f"Erreur: Impossible de convertir '{var_value}' en flottant")
                            continue
                    elif var_type == "str":
                        var_value = str(var_value)
                    elif var_type == "bin":
                        try:
                            var_value = int(var_value, 2)  # Conversion d'une chaîne binaire en entier
                        except ValueError:
                            output.append(f"Erreur: Impossible de convertir '{var_value}' en binaire")
                            continue
                    elif var_type == "hexa":
                        try:
                            var_value = int(var_value, 16)  # Conversion d'une chaîne hexadécimale en entier
                        except ValueError:
                            output.append(f"Erreur: Impossible de convertir '{var_value}' en hexadécimal")
                            continue
                    elif var_type == "bool":
                        # Vérification si la valeur est True ou False
                        if var_value.lower() == "true":
                            var_value = True
                        elif var_value.lower() == "false":
                            var_value = False
                        else:
                            output.append(f"Erreur: La valeur '{var_value}' n'est pas un booléen valide. Utilisez 'True' ou 'False'.")
                            continue             
                    else:
                        output.append(f"Erreur: Type '{var_type}' non supporté. Utilisez 'int', 'float', 'str', 'bin' ou 'bool'.")
                        continue

                    variables[var_name] = (var_type, var_value)
                else:
                    output.append("Erreur: La syntaxe de déclaration est 'set <nom> <type> <valeur>'")
            
            elif line.startswith("input"):
                parts = line[len("input "):].strip().split()
    
                if len(parts) == 3:
                    var_name = parts[0]
                    prompt = parts[1]
                    title = parts[2]

                    # Vérification que la variable existe avant d'afficher la fenêtre
                    if var_name not in variables:
                        output.append(f"Erreur: La variable '{var_name}' n'existe pas.")
                        continue
        
                    # Demander l'entrée utilisateur via tkinter
                    user_input = create_input_window(var_name, prompt, title)

                    # Vérification et conversion du type de la variable
                    var_type, _ = variables[var_name]
        
                    if var_type == "int":
                        try:
                            user_input = int(user_input)
                        except ValueError:
                            output.append(f"Erreur: Impossible de convertir '{user_input}' en entier.")
                            continue
                    elif var_type == "float":
                        try:
                            user_input = float(user_input)
                        except ValueError:
                            output.append(f"Erreur: Impossible de convertir '{user_input}' en flottant.")
                            continue
                    elif var_type == "str":
                        user_input = str(user_input)
                    elif var_type == "bin":
                        try:
                            user_input = int(user_input, 2)
                        except ValueError:
                            output.append(f"Erreur: Impossible de convertir '{user_input}' en binaire.")
                            continue
                    elif var_type == "bool":
                        if user_input.lower() == "true":
                            user_input = True
                        elif user_input.lower() == "false":
                            user_input = False
                        else:
                            output.append(f"Erreur: La valeur '{user_input}' n'est pas un booléen valide. Utilisez 'True' ou 'False'.")
                            continue

                    # Mise à jour de la variable avec la nouvelle valeur entrée
                    variables[var_name] = (var_type, user_input)

                else:
                    output.append("Erreur: La syntaxe de 'input' est 'input <nom_variable> <texte_prompt> <titre_fenetre>'")

            elif "~" in line:  # Si un commentaire est présent en ligne
                # Supprimer tout ce qui se trouve entre ~ et ~
                line = line.split("~")[0].strip()  # Tout avant le commentaire (ou la partie après ~)
                if not line:  # Si la ligne devient vide après suppression du commentaire, on l'ignore
                    continue

            elif line.startswith("mov"):
                parts = line[len("mov "):].strip().split()
                if len(parts) == 2:
                    dest_var = parts[0]
                    src_var = parts[1]

                    # Vérifier que la source existe
                    if src_var not in variables:
                        output.append(f"Erreur: La variable '{src_var}' n'est pas définie.")
                        continue
        
                    # Vérifier que la destination existe
                    if dest_var not in variables:
                        output.append(f"Erreur: La variable '{dest_var}' n'est pas définie.")
                        continue

                    # Vérifier que les types correspondent
                    src_type, src_value = variables[src_var]
                    dest_type, _ = variables[dest_var]
        
                    if src_type != dest_type:
                        output.append(f"Erreur: Les types des variables '{dest_var}' et '{src_var}' ne correspondent pas. Type attendu : '{dest_type}', mais trouvé : '{src_type}'.")
                        continue
        
                    # Copier la valeur de la variable source dans la variable destination
                    variables[dest_var] = (src_type, src_value)
        
                else:
                    output.append("Erreur: La syntaxe de 'mov' est 'mov <dest_var> <src_var>'")

            elif line.startswith("add"):
                parts = line[len("add "):].strip().split()
                if len(parts) == 2:
                    var_name = parts[0]
                    if var_name in variables:
                        var_type, var_value = variables[var_name]
                        if var_type == "int":
                            var_value += int(parts[1])
                            variables[var_name] = (var_type, var_value)
                        elif var_type == "float":
                            var_value += float(parts[1])
                            variables[var_name] = (var_type, var_value)
                        elif var_type == "bin":
                            var_value += int(parts[1], 2)
                            variables[var_name] = (var_type, var_value)
                        elif var_type == "hexa":
                            var_value += int(parts[1], 16)  # Soustraire une valeur binaire
                            variables[var_name] = (var_type, var_value)
                        else:
                            output.append(f"Erreur: Opération non valide pour le type {var_type} de '{var_name}'")
                    else:
                        output.append(f"Erreur: '{var_name}' n'est pas défini")
                else:
                    output.append("Erreur: Syntaxe incorrecte pour 'add'. Exemple: add <variable> <valeur>")

            elif line.startswith("sous"):
                parts = line[len("sous "):].strip().split()
                if len(parts) == 2:
                    var_name = parts[0]
                    if var_name in variables:
                        var_type, var_value = variables[var_name]
                        if var_type == "int":
                            var_value -= int(parts[1])
                            variables[var_name] = (var_type, var_value)
                        elif var_type == "float":
                            var_value -= float(parts[1])
                            variables[var_name] = (var_type, var_value)
                        elif var_type == "bin":
                            var_value -= int(parts[1], 2)  # Soustraire une valeur binaire
                            variables[var_name] = (var_type, var_value)
                        elif var_type == "hexa":
                            var_value -= int(parts[1], 16)  # Soustraire une valeur binaire
                            variables[var_name] = (var_type, var_value)
                        else:
                            output.append(f"Erreur: Opération non valide pour le type {var_type} de '{var_name}'")
                    else:
                        output.append(f"Erreur: '{var_name}' n'est pas défini")
                else:
                    output.append("Erreur: Syntaxe incorrecte pour 'sous'. Exemple: sous <variable> <valeur>")

            elif line.startswith("multi"):
                parts = line[len("multi "):].strip().split()
                if len(parts) == 2:
                    var_name = parts[0]
                    if var_name in variables:
                        var_type, var_value = variables[var_name]
                        if var_type == "int":
                            var_value *= int(parts[1])
                            variables[var_name] = (var_type, var_value)
                            output.append(f"Résultat: {var_value}")
                        elif var_type == "float":
                            var_value *= float(parts[1])
                            variables[var_name] = (var_type, var_value)
                            output.append(f"Résultat: {var_value}")
                        elif var_type == "bin":
                            var_value *= int(parts[1], 2)  # Multiplier par une valeur binaire
                            variables[var_name] = (var_type, var_value)
                            output.append(f"Résultat: {bin(var_value)}")
                        elif var_type == "hexa":
                            var_value *= int(parts[1], 16)  # Multiplier par une valeur binaire
                            variables[var_name] = (var_type, var_value)
                            output.append(f"Résultat: {hex(var_value)}")
                        else:
                            output.append(f"Erreur: Opération non valide pour le type {var_type} de '{var_name}'")
                    else:
                        output.append(f"Erreur: '{var_name}' n'est pas défini")
                else:
                    output.append("Erreur: Syntaxe incorrecte pour 'multi'. Exemple: multi <variable> <valeur>")

            elif line.startswith("div"):
                parts = line[len("div "):].strip().split()
                if len(parts) == 2:
                    var_name = parts[0]
                    if var_name in variables:
                        var_type, var_value = variables[var_name]
                        if var_type == "int":
                            if int(parts[1]) != 0:
                                var_value /= int(parts[1])
                                variables[var_name] = (var_type, var_value)
                            else:
                                output.append("Erreur: Division par zéro")
                        elif var_type == "float":
                            if float(parts[1]) != 0:
                                var_value /= float(parts[1])
                                variables[var_name] = (var_type, var_value)
                            else:
                                output.append("Erreur: Division par zéro")
                        elif var_type == "bin":
                            if int(parts[1], 2) != 0:
                                var_value /= int(parts[1], 2)  # Diviser par une valeur binaire
                                variables[var_name] = (var_type, var_value)
                        elif var_type == "hexa":
                            if int(parts[1], 16) != 0:
                                var_value /= int(parts[1], 16)  # Diviser par une valeur binaire
                                variables[var_name] = (var_type, var_value)
                            else:
                                output.append("Erreur: Division par zéro")
                        else:
                            output.append(f"Erreur: Opération non valide pour le type {var_type} de '{var_name}'")
                    else:
                        output.append(f"Erreur: '{var_name}' n'est pas défini")
                else:
                    output.append("Erreur: Syntaxe incorrecte pour 'div'. Exemple: div <variable> <valeur>")

            elif line.startswith("if"):
               # Récupérer la condition après "if"
                condition = line[len("if "):].strip()

                # Évaluer la condition
                try:
                    if eval(condition):  # Utilisation de `eval` pour évaluer la condition (sois prudent avec eval)
                        in_if_block = True  # Si la condition est vraie, entrer dans le bloc if
                    else:
                        in_if_block = False  # Sinon, ne pas entrer dans le bloc if
                except Exception as e:
                    output.append(f"Erreur dans l'évaluation de la condition '{condition}': {e}")
                    in_if_block = False

            elif line.startswith("-") and in_if_block:
                # Exécuter le code seulement si on est dans un bloc if valide
                line = line[1:].strip()  # Retirer le "-" du début de la ligne
                # Réexécuter les commandes normalement
                execute_code(line)

            elif line == "":
                # Si une ligne vide est rencontrée, l'ignorer (juste pour permettre une bonne gestion des blocs)
                continue


            elif line.startswith("while"):
                condition = line[len("while "):].strip()
                if ">" in condition:
                    var_name, value = condition.split(">")
                    var_name = var_name.strip()
                    value = int(value.strip())
        
                    if var_name in variables:
                        var_type, var_value = variables[var_name]
                        if var_type == "int" and var_value > value:
                            output.append(f"Condition 'while' vraie : {var_name} > {value}")
                            while var_value > value:  # Si la condition est vraie
                                output.append(f"Exécution dans la boucle while : {var_name} = {var_value}")
                                var_value -= 1  # Par exemple, on diminue la valeur pour simuler l'évolution
                                variables[var_name] = ("int", var_value)  # Mise à jour de la variable dans le dictionnaire
                        else:
                            output.append(f"Condition 'while' fausse : {var_name} <= {value}")
                    else:
                        output.append(f"Erreur: '{var_name}' n'est pas défini")
                else:
                    output.append(f"Erreur: Condition 'while' mal formée. Exemple : while x > 10")

            elif line.startswith("sav"):
                filename = line[len("sav "):].strip().strip('"')
                if filename:
                    with open("sacos/" + filename + ".SC", "w") as file:
                        file.write(code)
                    output.append(f"Code sauvegardé dans le fichier '{filename}.SC'")
                else:
                    output.append("Erreur: Nom de fichier manquant")

            elif line.startswith("load"):
                filename = line[len("load "):].strip().strip('"')
                if filename:
                    try:
                        with open("sacos/" + filename + ".SC", "r") as file:
                            loaded_code = file.read()
                        output.append(f"Code chargé depuis '{filename}.SC' :")
                        output.append(loaded_code)
                    except FileNotFoundError:
                        output.append(f"Erreur: Le fichier '{filename}.SC' n'a pas été trouvé")
                else:
                    output.append("Erreur: Nom de fichier manquant")

            elif line.startswith("Scode"):
                filename = "sacos/IDESC"
                if filename:
                    try:
                        with open(filename + ".py", "r") as file:
                            loaded_code = file.read()
                        output.append(f"Code chargé depuis '{filename}.SC' :")
                        output.append(loaded_code)
                    except FileNotFoundError:
                        output.append(f"Erreur: Le fichier '{filename}.SC' n'a pas été trouvé")
                else:
                    output.append("Erreur: Nom de fichier manquant")


            else:
                output.append(f"Erreur: commande non reconnue '{line}'")

        return "\n".join(output)

    except Exception as e:
        return f"Erreur d'exécution: {e}"


def execute_code():
    code = text_area.get("1.0", tk.END)  
    result = interpreter_sc(code)  
    console.delete(1.0, tk.END)
    console.insert(tk.END, result)  

root = tk.Tk()
root.title("Interpréteur SC")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

code_tab = ttk.Frame(notebook)
notebook.add(code_tab, text="Éditeur SC")

text_area = scrolledtext.ScrolledText(code_tab, height=21, width=125)
text_area.pack()

execute_button = tk.Button(code_tab, text="Exécuter", command=execute_code)
execute_button.pack()

console = scrolledtext.ScrolledText(code_tab, height=15, width=125)
console.pack()

help_tab = ttk.Frame(notebook)
notebook.add(help_tab, text="Aide")

help_text = """Bienvenue dans le langage SC !

Voici comment vous pouvez apprendre les bases :

1. taper load Tuto1

2. copier le code qui s'affiche dans la consle d'execution

3. ensuite une fois que vous avez analiser le code 
   vous pouvez creer un nouveau script et taper load 
   Tuto2 ...

4. En tous il y a 5 Tutos

Types de données disponibles :
- int : entier
- float : nombre à virgule flottante
- str : chaîne de caractères
- bin : binnaire
- bool : vrai ou faux

Si il y à des bug veuiller ne pas me tenire responsable si vous PETER votre PC en rageant

le code source du SC est du python (par se que je sais pas si 
j'avais le droit de faire du lua pour le launcharles)

Si vous avez des erreurs, elles seront affichées dans la console.

SC = SunrakuC (meme si les syntaxe n'ont rien avoire avec
le C ni avec n'importe quelle autre langage) 

mon objectif ULTIME avec se langage de code serait de faire un moteure de jeu car
j'ai la flemme d'apprendrele C#
(oui je suis un gros geek)

se langage à volontairement une syntaxe de "bas niveau" car 
j'aime beaucoup la programation de "bas niveau" comme le C ou l'assembly 
(meme si le SC est de beaucoup plus haut niveau que l'assembly)

BIG UP à tous les axolotl de France
"""
help_label = tk.Label(help_tab, text=help_text, justify="left", padx=10, pady=10)
help_label.pack()

root.mainloop()
