import os
import csv
from collections import Counter

def lire_csv(chemin_fichier_csv):
    event_ids = []

    with open(chemin_fichier_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            event_id = row['EventID']
            event_ids.append(event_id)

    return event_ids

def enumerer_event_ids(event_ids):
    compteur_event_ids = Counter(event_ids)

    print("Nombre d'occurrences pour chaque EventID :")
    for event_id, count in compteur_event_ids.items():
        print(f"EventID {event_id}: {count} occurrence(s)")

    print("\nEventIDs identiques :")
    for event_id, count in compteur_event_ids.items():
        if count > 1:
            print(f"EventID {event_id} est présent {count} fois.")

if __name__ == "__main__":
    chemin_fichier_csv = input("Veuillez entrer le chemin du fichier CSV à analyser : ")

    if not os.path.isfile(chemin_fichier_csv):
        print("Le fichier spécifié n'existe pas.")
        exit(1)

    event_ids = lire_csv(chemin_fichier_csv)

    if event_ids:
        enumerer_event_ids(event_ids)
    else:
        print("Aucun EventID trouvé dans le fichier CSV.")
