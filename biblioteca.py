import csv

def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    try:
        with open("biblioteca.csv", "r") as infile:
            with open(file_path, "r") as infile:
                prima_riga = infile.readline().strip()
                num_sezioni = int(prima_riga)
                biblioteca = [[] for _ in range(num_sezioni)]
        csv_reader = csv.reader(infile)
        for info in csv_reader:
            titolo = info[0]
            autore = info[1]
            anno = int(info[2])
            pagine = int(info[3])
            sezione = int(info[4])
            libro = {
                "titolo": titolo,
                "autore": autore,
                "anno": anno,
                "pagine": pagine,
                "sezione": sezione
            }
        biblioteca[sezione - 1].append(libro)
        biblioteca[sezione - 1].append(libro)
    except FileNotFoundError:
        print("File not found")
        return None
    return biblioteca


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO

    if sezione < 1 or sezione > len(biblioteca):
        return None
    titolo_ass=titolo.casefold()
    for lista in biblioteca:
        for libro in lista:
            if libro["titolo"].casefold()==titolo_ass:
                return None
    libro = {
    "titolo": titolo,
    "autore": autore,
    "anno": anno,
    "pagine": pagine,
    "sezione": sezione
    }
    biblioteca[sezione-1].append(libro)
    try:
        with open(file_path,"a",newline="", encoding="utf-8") as f:
         w = csv.writer(f)
         w.writerow([titolo,autore,anno,pagine,sezione])
    except FileNotFoundError :
        print("File not found")
        biblioteca[sezione - 1].pop()
        return None
    return libro


def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    titolo_cercato= titolo.casefold()
    for lista in biblioteca:
        for libro in lista:
            if libro["titolo"].casefold()==titolo_cercato:
                return libro
    return None


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    if sezione < 1 or sezione > len(biblioteca):
        return None
    lista_libri=biblioteca[sezione-1]
    titoli=[]
    for libro in lista_libri:
        titoli.append(libro["titolo"])
    titoli_ordinati = sorted(titoli, key=str.casefold)
    return titoli_ordinati


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()