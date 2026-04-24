import sqlite3
from datetime import date

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

def visualizza_libri():
    cursor.execute("SELECT * FROM libri")
    libri = cursor.fetchall()

    for libro in libri:
        print(f"ID: {libro[0]} | titolo: {libro[1]} | autore: {libro[2]} | anno: {libro[3]} | disponibile: {libro[4]} ")


def aggiungi_libro():
    
    titolo = input("Inserisci il titolo del libro da aggiungere: ")
    autore = input("Inserisci l'autore del libro da aggiungere")
    anno = int(input("Inserisci l'anno di pubblicazione del libro: "))
    
    cursor.execute("INSERT INTO libri (titolo, autore, anno, disponibile) VALUES (?, ?, ?, ?)", (titolo, autore, anno, 1))

    conn.commit()
    print("Libro aggiunto!")

    
def cerca_libro():

    cerca_titolo = input("Inserisci il titolo del libro che vuoi cercare: ")

    cursor.execute("SELECT * FROM libri WHERE titolo LIKE ?", (f"%{cerca_titolo}%",))

    libri = cursor.fetchall()

    for libro in libri:
        print(f"ID: {libro[0]} | titolo: {libro[1]} | autore: {libro[2]} | anno: {libro[3]} | disponibile: {libro[4]} ")


def registra_prestito():
    
    visualizza_libri()
    
    data_oggi = str(date.today())

    cursor.execute("SELECT * FROM libri WHERE disponibile = 1")

    cerca_id = int(input("Inserisci l'ID del libro da prendere: "))
    cursor.execute("UPDATE libri SET disponibile = 0 WHERE id = ?", (cerca_id,))

    id_utente = int(input("Inserisci il tuo ID utente per la registrazione del prestito: "))
    cursor.execute("INSERT INTO prestiti (libro_id, utente_id, data_prestito) VALUES (?, ?, ?)", (cerca_id, id_utente, data_oggi))

    conn.commit()
    print("Prestito registrato correttamente!")


def restituisci_libro():
    cerca_id = int(input("Inserisci l'ID del libro da restituire: "))

    cursor.execute("UPDATE libri SET disponibile = 1 WHERE id = ?", (cerca_id,))
    cursor.execute("DELETE FROM prestiti WHERE libro_id = ?", (cerca_id,))

    conn.commit()
    print("Libro restituito!")


while True:

    print("1 - Visualizza Libri ")
    print("2 - Aggiungi Libro")
    print("3 - Cerca Libro")
    print("4 - Registra Prestito")
    print("5 - Restituisci Libro")
    print("6 - Esci")

    scelta = input("Cosa vuoi fare?")

    if scelta == "1":
        visualizza_libri()

    elif scelta == "2":
        aggiungi_libro()

    elif scelta == "3":
        cerca_libro()

    elif scelta == "4":
        registra_prestito()

    elif scelta == "5":
        restituisci_libro()

    else:
        break