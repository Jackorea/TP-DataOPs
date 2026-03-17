# Requêtes HTTP pour récupérer les données
import requests

# Identifiant du jeu de données DNMA (par UAI, profils, appareils)
DATASET_ID = "fr-en-dnma-par-uai-profils-appareils"
# URL d'export CSV du catalogue data.education.gouv.fr
CSV_EXPORT_URL = f"https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/{DATASET_ID}/exports/csv"

# En-tête pour identifier le client (éviter le blocage par certains serveurs)
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; DNMA-CSV-Counter/1.0)"}


def count_lines_from_url(url: str) -> int:
    """Compte le nombre de lignes d'un fichier CSV accessible par URL (en flux)."""
    r = requests.get(url, headers=HEADERS, stream=True)
    r.raise_for_status()
    return sum(1 for _ in r.iter_lines())


def main() -> None:
    """Affiche les infos du dataset et le total de lignes du CSV exporté."""
    print(f"Dataset: {DATASET_ID}")
    print(f"URL: {CSV_EXPORT_URL}")
    try:
        total = count_lines_from_url(CSV_EXPORT_URL)
        print(f"Total lignes: {total}")
    except requests.RequestException as e:
        print(f"Erreur: {e}")
        raise SystemExit(1)


# Point d'entrée du script
if __name__ == "__main__":
    main()
