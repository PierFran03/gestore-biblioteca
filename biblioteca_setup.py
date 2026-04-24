import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("""

    CREATE TABLE IF NOT EXISTS libri(
               
               id INTEGER PRIMARY KEY,
               titolo TEXT,
               autore TEXT,
               anno INTEGER,
               disponibile INTEGER   
               
               )

""")

cursor.execute("""

    CREATE TABLE IF NOT EXISTS utenti(
               
               id INTEGER PRIMARY KEY,
               nome TEXT,
               cognome TEXT

    )

""")

cursor.execute("""

    CREATE TABLE IF NOT EXISTS prestiti(
               
               id INTEGER PRIMARY KEY,
               libro_id INTEGER,
               utente_id INTEGER,
               data_prestito TEXT               
               
    )

""")

conn.commit()

cursor.execute("INSERT INTO libri (titolo, autore, anno, disponibile) VALUES (?, ?, ?, ?)", ("Il Nome della Rosa", "Umberto Eco", 1980, 1))
cursor.execute("INSERT INTO libri (titolo, autore, anno, disponibile) VALUES (?, ?, ?, ?)", ("1984", "George Orwell", 1949, 1))
cursor.execute("INSERT INTO utenti (nome, cognome) VALUES (?, ?)", ("Mario", "Rossi"))
cursor.execute("INSERT INTO utenti (nome, cognome) VALUES (?, ?)", ("Anna", "Bianchi"))

conn.commit()
conn.close()
print("Database biblioteca creato con successo!")