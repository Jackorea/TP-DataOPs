"""
EB4 : Comparer plusieurs UAIs pour une année donnée.
Affiche un tableau comparatif avec le nombre total de visites et la répartition par appareil.
"""

import pandas as pd
import sys

# Récupérer les arguments
annee = int(sys.argv[1])
uais = sys.argv[2:]

# Charger les données
colonnes = ['debutSemaine', 'UAI', 'visites_ordinateur', 'visites_smartphone', 
            'visites_tablette', 'visites_autreappareil']
df = pd.read_csv('dnma.csv', sep=';', usecols=colonnes)

# Convertir et filtrer
df['debutSemaine'] = pd.to_datetime(df['debutSemaine'], format='%Y-%m-%d')
df_filtered = df[(df['UAI'].isin(uais)) & (df['debutSemaine'].dt.year == annee)].copy()

# Calculer le total de visites
df_filtered['total_visites'] = (
    df_filtered['visites_ordinateur'] + 
    df_filtered['visites_smartphone'] + 
    df_filtered['visites_tablette'] + 
    df_filtered['visites_autreappareil']
)

# Agréger par UAI
df_resultat = df_filtered.groupby('UAI').agg({
    'total_visites': 'sum',
    'visites_ordinateur': 'sum',
    'visites_smartphone': 'sum',
    'visites_tablette': 'sum'
}).reset_index()

# Calculer les pourcentages
df_resultat['% Ordinateur'] = (df_resultat['visites_ordinateur'] / df_resultat['total_visites'] * 100).round(2)
df_resultat['% Smartphone'] = (df_resultat['visites_smartphone'] / df_resultat['total_visites'] * 100).round(2)
df_resultat['% Tablette'] = (df_resultat['visites_tablette'] / df_resultat['total_visites'] * 100).round(2)

# Trier et afficher
df_resultat = df_resultat.sort_values('total_visites', ascending=False)

print(f"\nComparaison des UAIs pour l'année {annee}\n")
print(df_resultat[['UAI', 'total_visites', 'visites_ordinateur', 'visites_smartphone', 'visites_tablette', 
                   '% Ordinateur', '% Smartphone', '% Tablette']].to_string(index=False))
