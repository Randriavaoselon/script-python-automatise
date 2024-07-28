import tkinter as tk
import webbrowser
from urllib.parse import urlencode
import requests

# Fonction pour générer les URLs de recherche Google et ouvrir le navigateur
def open_google_search():
    query = entry.get()
    keywords = keywords_entry.get()  # Récupère les mots clés supplémentaires
    num_results = int(results_entry.get() or 10)  # Nombre de résultats par page, par défaut 10
    num_pages = int(pages_entry.get() or 1)       # Nombre de pages, par défaut 1
    
    if query:
        full_query = f"{query} {keywords}"  # Combine la requête principale avec les mots clés
        for page in range(num_pages):
            start_index = page * num_results  # Calculer le point de départ pour chaque page
            # Paramètres de la recherche
            params = {
                "q": full_query,
                "hl": "fr",   # Langue des résultats
                "gl": "fr",   # Pays des résultats
                "num": num_results,  # Nombre de résultats par page
                "start": start_index # Point de départ pour la pagination
            }
            # Encode les paramètres pour l'URL
            url_params = urlencode(params)
            # URL de recherche Google
            google_url = f"https://www.google.com/search?{url_params}"
            
            # Utiliser un proxy pour accéder à Google
            proxy = {
                "https": "http://43.133.173.132:3128" # Voici l'adresse IP d'un proxy public que j'ai pris sur internet
            }
            try:
                response = requests.get(google_url, proxies=proxy, timeout=300)
                webbrowser.open(response.url, new=2)  # `new=2` pour ouvrir dans une nouvelle fenêtre
            except Exception as e:
                print(f"Error: {e}")

# Configuration de l'interface Tkinter
root = tk.Tk()
root.title("Google Search Opener")

# Zone de saisie pour la recherche principale
tk.Label(root, text="Recherche principale:").pack(padx=10, pady=5)
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

# Zone de saisie pour les mots clés
tk.Label(root, text="Mots clés supplémentaires:").pack(padx=10, pady=5)
keywords_entry = tk.Entry(root, width=50)
keywords_entry.pack(padx=10, pady=5)

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