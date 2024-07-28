import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
import webbrowser

# Fonction pour effectuer la recherche Google et extraire les résultats
def search_google():
    query = entry.get()
    if not query:
        messagebox.showwarning("Avertissement", "Veuillez entrer une requête.")
        return

    # Paramètres de la requête Google
    params = {
        "q": query,
        "hl": "fr",  # langue
        "gl": "fr",  # pays de la recherche, FR -> France
        "start": 0
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    try:
        html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
        soup = BeautifulSoup(html.text, 'lxml')

        results = []
        for result in soup.select(".tF2Cxc"):
            title = result.select_one(".DKV0Md").text
            snippet = result.select_one(".lEBKkf span")
            snippet = snippet.text if snippet else "Pas de description disponible."
            link = result.select_one(".yuRUbf a")["href"]

            results.append({
                "title": title,
                "snippet": snippet,
                "link": link
            })

        display_results(results)

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

# Fonction pour afficher les résultats dans l'interface tkinter
def display_results(results):
    for row in tree.get_children():
        tree.delete(row)
    
    for result in results:
        tree.insert("", tk.END, values=(result["title"], result["snippet"], result["link"]))

# Fonction pour ouvrir le lien sélectionné dans le navigateur
def open_link(event):
    selected_item = tree.selection()
    if selected_item:
        link = tree.item(selected_item[0], 'values')[2]  # Récupère le lien de la colonne "Link"
        webbrowser.open(link)

# Création de la fenêtre principale
window = tk.Tk()
window.title("Recherche Google avec Affichage des Résultats")

# Création d'un label d'instruction
label = tk.Label(window, text="Entrez votre recherche Google :")
label.pack(pady=5)

# Création du champ de texte
entry = tk.Entry(window, width=50)
entry.pack(padx=20, pady=10)

# Création du bouton de recherche
button = tk.Button(window, text="Rechercher", command=search_google)
button.pack(pady=10)

# Création d'un Treeview pour afficher les résultats
tree = ttk.Treeview(window, columns=("Title", "Snippet", "Link"), show="headings", height=10)
tree.heading("Title", text="Titre")
tree.heading("Snippet", text="Extrait")
tree.heading("Link", text="Lien")
tree.column("Title", width=250)
tree.column("Snippet", width=400)
tree.column("Link", width=300)
tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Associer l'événement de double-clic à l'ouverture du lien dans le navigateur
tree.bind("<Double-1>", open_link)

# Lancement de la boucle principale de la fenêtre
window.mainloop()