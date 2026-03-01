# Analyse du Jeu de Données DNMA par UAI et Appareils

## Partie Théorique

### 1. Présentation du DNMA

Le **DNMA (Dispositif National de Mesure d'Audience)** est un système de mesure d'audience web mis en place par le Ministère de l'Éducation Nationale pour suivre et analyser l'utilisation des sites web éducatifs. Il permet de collecter des données anonymisées sur les visites, les utilisateurs et la durée de navigation sur les sites web des établissements scolaires français. Ces données sont agrégées par établissement (identifié par son UAI) et permettent d'analyser les comportements de navigation selon différents critères : type d'appareil, système d'exploitation, navigateur web, etc.

### 2. Définition du terme UAI

L'**UAI (Unité Administrative Immatriculée)** est un code d'identification unique attribué à chaque établissement scolaire français. Ce code alphanumérique de 8 caractères (par exemple : 0010024W, 0220158C) permet d'identifier de manière univoque un établissement d'enseignement, qu'il s'agisse d'une école primaire, d'un collège, d'un lycée, ou d'un établissement d'enseignement supérieur. L'UAI est utilisé dans toutes les bases de données administratives de l'Éducation Nationale pour référencer les établissements.

### 3. Analyse du jeu de données

#### a. Présentation des données incluses

**Lien vers le jeu de données :** [DNMA par UAI et Appareils](https://data.education.gouv.fr/explore/assets/fr-en-dnma-par-uai-appareils/)

Le jeu de données DNMA contient des statistiques d'audience web agrégées par établissement scolaire et par semaine. Chaque ligne représente les données d'un établissement (identifié par son code UAI) pour une semaine donnée.

**Nature des données collectées :**
- **Données d'identification** : Informations permettant d'identifier et de localiser l'établissement (UAI, académie, commune, département, région, etc.)
- **Données temporelles** : Date de début de la semaine de mesure (`debutSemaine`)
- **Métriques d'audience** : Pour chaque dimension d'analyse (type d'appareil, système d'exploitation, navigateur), trois types de métriques sont collectés :
  - **Visites** : Nombre total de sessions/visites enregistrées
  - **Utilisateurs** : Nombre d'utilisateurs uniques
  - **Durée** : Temps total de navigation (format HH:MM:SS)

**Dimensions d'analyse disponibles :**
- **Par type d'appareil** : Ordinateur, smartphone, tablette, autres appareils
- **Par système d'exploitation** : Android, Windows, iOS, macOS, ChromeOS, Linux, autres OS
- **Par navigateur web** : Chrome Mobile, Safari, Chrome, Firefox, Edge, Samsung Browser, Opera, Huawei Browser, MIUI Browser, autres navigateurs

Le jeu de données permet ainsi d'analyser les comportements de navigation des utilisateurs des sites web éducatifs selon différentes perspectives, offrant une vue détaillée de l'utilisation des ressources numériques par les établissements scolaires français.


#### b. Catégorisation des colonnes du JDD

Le jeu de données comprend **73 colonnes** au total, qui peuvent être organisées en 4 catégories principales selon leur fonction et leur type de données :

**1. Colonnes temporelles et d'identification (10 colonnes)**
- `debutSemaine` : Date de début de la semaine (format YYYY-MM-DD)
- `UAI` : Code d'identification unique de l'établissement
- `académie` : Nom de l'académie
- `commune` : Nom de la commune
- `département` : Nom du département
- `région` : Nom de la région
- `ministère` : Ministère de tutelle
- `circonscription` : Circonscription administrative (peut être vide)
- `nature_uai` : Type d'établissement (ex: Collège, Lycée, Ecole élémentaire, etc.)
- `secteur` : Secteur (PU = Public, PR = Privé)

**2. Colonnes métriques par type d'appareil (12 colonnes)**
- `visites_ordinateur`, `utilisateurs_ordinateur`, `duree_ordinateur`
- `visites_smartphone`, `utilisateurs_smartphone`, `duree_smartphone`
- `visites_tablette`, `utilisateurs_tablette`, `duree_tablette`
- `visites_autreappareil`, `utilisateurs_autreAppareil`, `duree_autreAppareil`

**3. Colonnes métriques par système d'exploitation (21 colonnes)**
- Pour chaque OS (android, windows, ios, macos, chromeos, linux, autreOS) :
  - `visites_[OS]`, `utilisateurs_[OS]`, `duree_[OS]`

**4. Colonnes métriques par navigateur web (30 colonnes)**
- Pour chaque navigateur (chromeMobile, safari, chrome, firefox, edge, samsungBrowser, opera, huaweiBrowser, miuiBrowser, autreNavigateur) :
  - `visites_[navigateur]`, `utilisateurs_[navigateur]`, `duree_[navigateur]`

**Structure des métriques** :
- **Visites** : Nombre total de visites/sessions
- **Utilisateurs** : Nombre d'utilisateurs uniques
- **Durée** : Durée totale de navigation (format HH:MM:SS)

### 4. Différences entre le premier JDD et les JDD suivants (JDD2, JDD3)

Les trois jeux de données (JDD1, JDD2, JDD3) partagent une structure commune avec les colonnes d'identification (`debutSemaine`, `UAI`, et les informations géographiques/administratives), mais diffèrent fondamentalement par **l'angle d'analyse** des métriques d'audience :

#### JDD1 - Analyse technique (73 colonnes)
**Perspective :** Analyse selon les caractéristiques techniques des appareils et logiciels utilisés
- **Par type d'appareil** : Ordinateur, smartphone, tablette, autres appareils (12 colonnes)
- **Par système d'exploitation** : Android, Windows, iOS, macOS, ChromeOS, Linux, autres OS (21 colonnes)
- **Par navigateur web** : Chrome Mobile, Safari, Chrome, Firefox, Edge, Samsung Browser, Opera, Huawei Browser, MIUI Browser, autres navigateurs (30 colonnes)

**Structure :** 10 colonnes d'identification + 63 colonnes de métriques techniques

#### JDD2 - Analyse par services/fonctionnalités (85 colonnes)
**Perspective :** Analyse selon les services et fonctionnalités numériques utilisés
- **Services analysés** (25 services) :
  - Services généraux : `accueil`, `actualites`
  - Communication : `cahier_textes`, `cahier_liaison`, `courrier_electronique`, `messagerie_instantanee`, `visioconference`
  - Collaboration : `stockage_partage`, `production_collaborative`
  - Pédagogie : `documentation_cdi`, `parcours_pedagogique`
  - Gestion : `reservation_salles_materiels`, `service_collectivite`, `services_vie_scolaire`, `gestion_temps`, `absences`, `gestion_competences`, `notes`
  - Ressources : `manuel_numerique`, `ressource_multimedia`, `ressource_orientation`, `ressource_production`, `ressource_accompagnement_entrainement`, `ressource_reference_dictionnaire`, `ressource_documentaire`

**Structure :** `debutSemaine` + `UAI` + 75 colonnes de métriques par service (25 services × 3 métriques) + 8 colonnes d'identification en fin de fichier

#### JDD3 - Analyse par profil utilisateur (25 colonnes)
**Perspective :** Analyse selon le profil/rôle des utilisateurs
- **Profils analysés** (5 profils) :
  - `globales` : Tous les utilisateurs confondus
  - `eleve` : Élèves
  - `parent` : Parents
  - `enseignant` : Enseignants
  - `admin_vie_scol_tech` : Administrateurs, personnels de vie scolaire et techniques

**Structure :** 10 colonnes d'identification + 15 colonnes de métriques par profil (5 profils × 3 métriques)

#### Synthèse des différences

| Caractéristique | JDD1 | JDD2 | JDD3 |
|----------------|------|------|------|
| **Angle d'analyse** | Technique (appareil/OS/navigateur) | Fonctionnel (services) | Utilisateur (profil/rôle) |
| **Nombre de colonnes** | 73 | 85 | 25 |
| **Nombre de dimensions** | 3 (appareil, OS, navigateur) | 1 (service) | 1 (profil) |
| **Position des colonnes d'identification** | Au début | `debutSemaine` et `UAI` au début, autres à la fin | Au début |
| **Granularité** | Très détaillée (63 métriques) | Très détaillée (75 métriques) | Moins détaillée (15 métriques) |

Ces trois jeux de données sont **complémentaires** et permettent d'analyser l'utilisation des ressources numériques éducatives sous différents angles : comment les utilisateurs accèdent (JDD1), quels services ils utilisent (JDD2), et qui les utilise (JDD3).


---

# TP-DataOPs
# TP-DataOPs
# TP-DataOPs
