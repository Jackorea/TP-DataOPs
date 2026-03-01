"""
EB3 : Créer un script qui prend en entrée l'UAI et l'année et afficher un graphique 
présentant l'évolution par mois du nombre de visites selon les appareils 
tablette/smartphone/ordinateur.
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys

# Récupérer les paramètres en entrée
uai = sys.argv[1]
annee = int(sys.argv[2])

# Charger le fichier CSV
colonnes_necessaires = ['debutSemaine', 'UAI', 'visites_ordinateur', 
                       'visites_smartphone', 'visites_tablette']
df = pd.read_csv('dnma.csv', sep=';', usecols=colonnes_necessaires)

# Convertir la colonne debutSemaine en datetime
df['debutSemaine'] = pd.to_datetime(df['debutSemaine'], format='%Y-%m-%d')

# Filtrer par UAI et année
df_filtered = df[
    (df['UAI'] == uai) & 
    (df['debutSemaine'].dt.year == annee)
].copy()

# Créer une colonne pour le mois
df_filtered['mois'] = df_filtered['debutSemaine'].dt.to_period('M').astype(str)

# Agréger par mois
df_agrege = df_filtered.groupby('mois').agg({
    'visites_ordinateur': 'sum',
    'visites_smartphone': 'sum',
    'visites_tablette': 'sum'
}).reset_index()

# Trier par mois
df_agrege = df_agrege.sort_values('mois')

# Créer le graphique
plt.figure(figsize=(12, 6))
plt.plot(df_agrege['mois'], df_agrege['visites_ordinateur'], 
         marker='o', label='Ordinateur', linewidth=2, markersize=6)
plt.plot(df_agrege['mois'], df_agrege['visites_smartphone'], 
         marker='s', label='Smartphone', linewidth=2, markersize=6)
plt.plot(df_agrege['mois'], df_agrege['visites_tablette'], 
         marker='^', label='Tablette', linewidth=2, markersize=6)

plt.title(f'Évolution du nombre de visites par mois - UAI: {uai} - Année: {annee}')
plt.xlabel('Mois')
plt.ylabel('Nombre de visites')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Afficher le graphique
plt.show()

