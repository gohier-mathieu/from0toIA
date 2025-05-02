import pandas as pd
import matplotlib.pyplot as plt

# Chargement du fichier CSV contenant les données météo
df = pd.read_csv('meteo.csv')

# Récupération de la liste des villes (toutes les colonnes sauf la première, "Mois")
villes = df.columns[1:]

# Demande à l'utilisateur de choisir une ville ou d'afficher toutes les villes
ville = input("Entrez une ville (Paris, Lyon, Marseille, Lille, Toulouse) ou 'toutes' : ").capitalize()

# Vérifie si l'entrée est valide (ville existante ou 'toutes')
if ville == 'Toutes':
    # Affiche toutes les villes sur le même graphique
    for v in villes:
        plt.plot(df['Mois'], df[v], label=v)
    plt.title("Températures mensuelles moyennes dans 5 villes françaises")
else:
    if ville not in villes:
        print(f"Erreur : la ville '{ville}' n'existe pas dans les données.")
    else:
        # Affiche uniquement la ville choisie
        plt.plot(df['Mois'], df[ville], label=ville)
        plt.title(f"Températures mensuelles moyennes à {ville}")

# Paramètres du graphique (si une ville valide a été tracée)
if ville == 'Toutes' or ville in villes:
    plt.xlabel("Mois")
    plt.ylabel("Température (°C)")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)  # Pour lisibilité des mois
    plt.tight_layout()       # Pour éviter que le texte déborde
    plt.show()
