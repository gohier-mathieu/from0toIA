import csv

def calculer_moyenne(notes):
    return sum(notes) / len(notes)



def main():
    # lire le fichier.csv
    with open('etudiants_notes.csv', mode='r', newline='', encoding='utf-8') as fichier_csv:
        notes = csv.reader(fichier_csv)
        # ignorer la premiere ligne
        next(notes)
        for ligne in notes:
            #extraire les notes sans le 1er element
            valeurs_notes = ligne[1:]

            # convertir note de string a float 
            notes_numeriques = [float(note) for note in valeurs_notes]

            # calculer la moyenne 
            moyenne = calculer_moyenne(notes_numeriques)

            print(f"{ligne[0]} a une moyenne de {moyenne:.2f}")


if __name__ == "__main__":
    main()