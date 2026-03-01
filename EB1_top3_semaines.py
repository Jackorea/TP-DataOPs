"""
EB1 : Calculer et afficher dans un tableau (Semaine | Nb Visites) 
avec les 3 semaines ayant le plus grand nombre de visites pour l'UAI 0010024W dans l'année 2025.
"""

import pandas as pd

# Paramètres fixes selon les exigences
UAI = "0010024W"
ANNEE = 2025

# Charger le fichier CSV
colonnes_necessaires = ['debutSemaine', 'UAI', 'visites_ordinateur', 'visites_smartphone', 
                       'visites_tablette', 'visites_autreappareil']
df = pd.read_csv('dnma.csv', sep=';', usecols=colonnes_necessaires)

# Convertir la colonne debutSemaine en datetime
df['debutSemaine'] = pd.to_datetime(df['debutSemaine'], format='%Y-%m-%d')

# Filtrer par UAI et année
df_filtered = df[
    (df['UAI'] == UAI) & 
    (df['debutSemaine'].dt.year == ANNEE)
].copy()

# Calculer le nombre total de visites par semaine
df_filtered['nb_visites_total'] = (
    df_filtered['visites_ordinateur'] +
    df_filtered['visites_smartphone'] +
    df_filtered['visites_tablette'] +
    df_filtered['visites_autreappareil']
)

# Trier par nombre de visites décroissant et prendre les 3 premières
df_top3 = df_filtered.nlargest(3, 'nb_visites_total')

# Formater pour l'affichage
df_top3['Semaine'] = df_top3['debutSemaine'].dt.strftime('%Y-%m-%d')
df_top3['Nb Visites'] = df_top3['nb_visites_total']

# Afficher le tableau
resultat = df_top3[['Semaine', 'Nb Visites']]
print(resultat.to_string(index=False))
