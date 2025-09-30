# Lab 02

#### Argomenti

- Liste di liste: iterazioni e ordinamenti.
- Lettura da e scrittura su file.
- Eccezioni.


## Biblioteca
Progettare e realizzare un programma che possa essere utilizzato per la catalogazione dei libri in una biblioteca. 
Le biblioteca è composta da diverse sezioni identificate da un numero intero (sezione 1, sezione 2, ecc.). 
Ogni sezione contiene dei libri. 
Ogni libro è univocamente identificato dal titolo, e caratterizzato da autore, anno di pubblicazione e numero di pagine. 
I libri vengono collocati nelle sezioni. 

Viene fornito un file chiamato `biblioteca.csv` che contiene un elenco di libri. La prima riga del file contiene il 
numero di sezioni della biblioteca. Dalla seconda riga in poi sono riportate le informazioni inerenti a ciascun libro 
(titolo, autore, anno di pubblicazione, pagine, numero della sezione), uno per riga. 

Esempio di file `biblioteca.csv`:
```file
5
I Promessi Sposi,Alessandro Manzoni,1827,720,1 
Cuore,Edmondo De Amicis,1886,300,1 
Divina Commedia,Dante Alighieri,1321,798,2 
Moby Dick, Herman Melville,1851,635,2
...
```

### Implementazione
Per questo laboratorio è necessario implementare le funzioni presenti nel file `biblioteca.py` e modellare il concetto 
di libro utilizzando una struttura dati opportuna (una lista, una tupla, un dizionario, una classe, ecc.).

La funzione `main()` presente nel file `biblioteca.py` consente di interagire con il sistema tramite un menù testuale 
utilizzabile dalla console. 

```menu in console
1. Carica biblioteca da file 
2. Aggiungi un nuovo libro 
3. Cerca un libro per titolo 
4. Ordina titoli di una sezione
5. Esci
Scegli un'opzione >>
```

Il menu permette di effettuare varie operazioni che devono essere gestite da opportune funzioni. 

La funzione `carica_da_file()` riceve come parametro il percorso del file da leggere e deve creare e popolare una 
struttura dati che rappresenta la biblioteca distribuendo i libri presenti nel file nelle sezioni corrette. 
La funzione deve restituire la struttura dati creata. Se l’apertura del file scatena l’eccezione `FileNotFoundError`, 
la funzione deve restituire `None`. 

L'aggiunta di un nuovo libro non già presente nella biblioteca viene gestita tramite la funzione `aggiungi_libro()`, 
che riceve come parametri la struttura dati rappresentante la biblioteca, il titolo del libro, l'autore, l'anno di 
pubblicazione, il numero di pagine, la sezione e il percorso del file da aggiornare. La funzione deve aggiornare la 
struttura dati ed il file, inserendo una nuova riga in fondo a quest'ultimo. In caso di aggiornamento avvenuto con successo, 
la funzione deve ritornare un riferimento al libro aggiunto. In caso errori, quali titolo già presente, sezione non 
esistente o file non trovato, la funzione deve restituire `None`.   

Per accedere alle informazioni relative ad uno qualsiasi dei libri memorizzati si utilizza la funzione `cerca_libro()`, 
che riceve come parametro la struttura dati rappresentante la biblioteca ed il titolo del libro da cercare. 
Nel caso in cui il libro non esista, la funzione restituisce `None`; altrimenti, restituisce una stringa contenente il 
titolo, l'autore, l'anno di pubblicazione, il numero di pagine e la sezione in cui si trova il libro, nel il seguente 
formato: 

```formato
I Promessi Sposi, Alessandro Manzoni, 1827, 720, 1
```

Il sistema, attraverso la funzione `elenco_libri_sezione_per_titolo()`, consente di ottenere un elenco dei libri 
presenti in una specifica sezione della biblioteca ordinati alfabeticamente. La funzione riceve come parametri 
la struttura dati che rappresenta la biblioteca e il numero della sezione da ordinare. Una volta eseguita l’operazione, 
il sistema restituisce la lista dei titoli di quella sezione in ordine alfabetico. Nel caso in cui la sezione non 
esista, la funzione restituisce `None`. 
