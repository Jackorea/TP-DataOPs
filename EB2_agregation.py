"""
EB2 : Créer un script qui prend en entrée une UAI et une granularité ("Année", "Mois"),
agréger les données suivant ce critère et afficher les résultats dans un tableau.
"""

import pandas as pd
import sys

# Récupérer les paramètres en entrée
uai = sys.argv[1]
granularite = sys.argv[2]

# Charger le fichier CSV
colonnes_necessaires = ['debutSemaine', 'UAI', 'visites_ordinateur', 'visites_smartphone', 
                       'visites_tablette', 'visites_autreappareil']
df = pd.read_csv('dnma.csv', sep=';', usecols=colonnes_necessaires)

# Convertir la colonne debutSemaine en datetime
df['debutSemaine'] = pd.to_datetime(df['debutSemaine'], format='%Y-%m-%d')

# Filtrer par UAI
df_filtered = df[df['UAI'] == uai].copy()

# Calculer le nombre total de visites
df_filtered['nb_visites_total'] = (
    df_filtered['visites_ordinateur'] +
    df_filtered['visites_smartphone'] +
    df_filtered['visites_tablette'] +
    df_filtered['visites_autreappareil']
)

# Agrégation selon la granularité
if granularite.lower() == "année":
    df_filtered['periode'] = df_filtered['debutSemaine'].dt.year
elif granularite.lower() == "mois":
    df_filtered['periode'] = df_filtered['debutSemaine'].dt.to_period('M').astype(str)

# Agréger les données
df_agrege = df_filtered.groupby('periode').agg({
    'nb_visites_total': 'sum',
    'visites_ordinateur': 'sum',
    'visites_smartphone': 'sum',
    'visites_tablette': 'sum',
    'visites_autreappareil': 'sum'
}).reset_index()

# Afficher le tableau
print(df_agrege.to_string(index=False))
