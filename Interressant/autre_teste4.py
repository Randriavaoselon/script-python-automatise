import tkinter as tk
import webbrowser
from urllib.parse import urlencode

# Fonction pour générer l'URL de recherche Google et ouvrir le navigateur
def open_google_search():
    query = entry.get()
    if query:
        # Paramètres de la recherche
        params = {
            "q": query,
            "hl": "fr",  # Langue des résultats
            "gl": "fr",  # Pays des résultats
        }
        # Encode les paramètres pour l'URL
        url_params = urlencode(params)
        # URL de recherche Google
        google_url = f"https://www.google.com/search?{url_params}"
        # Ouvre l'URL dans le navigateur par défaut
        webbrowser.open(google_url)

# Configuration de l'interface Tkinter
root = tk.Tk()
root.title("Google Search Opener")

# Zone de saisie pour la recherche
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=10)

# Bouton pour lancer la recherche
search_button = tk.Button(root, text="Search", command=open_google_search)
search_button.pack(padx=10, pady=10)

# Démarre la boucle principale Tkinter
root.mainloop()