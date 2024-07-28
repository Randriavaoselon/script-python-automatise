import tkinter as tk
import webbrowser
from urllib.parse import urlencode

# Fonction pour générer les URLs de recherche Google et ouvrir le navigateur
def open_google_search():
    query = entry.get()
    num_results = int(results_entry.get() or 10)  # Nombre de résultats par page, par défaut 10
    num_pages = int(pages_entry.get() or 1)       # Nombre de pages, par défaut 1
    
    if query:
        for page in range(num_pages):
            start_index = page * num_results  # Calculer le point de départ pour chaque page
            # Paramètres de la recherche
            params = {
                "q": query,
                "hl": "fr",   # Langue des résultats
                "gl": "fr",   # Pays des résultats
                "num": num_results,  # Nombre de résultats par page
                "start": start_index # Point de départ pour la pagination
            }
            # Encode les paramètres pour l'URL
            url_params = urlencode(params)
            # URL de recherche Google
            google_url = f"https://www.google.com/search?{url_params}"
            # Ouvre l'URL dans le navigateur par défaut
            webbrowser.open(google_url, new=2)  # `new=2` pour ouvrir dans une nouvelle fenêtre

# Configuration de l'interface Tkinter
root = tk.Tk()
root.title("Google Search Opener")

# Zone de saisie pour la recherche
tk.Label(root, text="Recherche:").pack(padx=10, pady=5)
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

# Zone de saisie pour le nombre de résultats par page
tk.Label(root, text="Nombre de résultats par page (1-100):").pack(padx=10, pady=5)
results_entry = tk.Entry(root, width=10)
results_entry.pack(padx=10, pady=5)

# Zone de saisie pour le nombre de pages
tk.Label(root, text="Nombre de pages:").pack(padx=10, pady=5)
pages_entry = tk.Entry(root, width=10)
pages_entry.pack(padx=10, pady=5)

# Bouton pour lancer la recherche
search_button = tk.Button(root, text="Search", command=open_google_search)
search_button.pack(padx=10, pady=10)

# Démarre la boucle principale Tkinter
root.mainloop()
