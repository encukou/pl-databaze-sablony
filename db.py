import os
import sqlite3

# Smaže soubor s databází, pokud existuje
try:
    os.unlink('blog.db')
except OSError:
    pass

conn = sqlite3.connect('blog.db')

c = conn.cursor()

c.execute('''
    CREATE TABLE clanky
    (id INTEGER PRIMARY KEY,
     nazev TEXT,
     obsah TEXT,
     autor INT)
''')

c.execute('''
    CREATE TABLE autori
    (id INTEGER PRIMARY KEY,
     jmeno TEXT,
     prijmeni TEXT)
''')

for i in range(10):
    jmeno = 'Franta' + str(i)
    prijmeni = 'Vomáčka' + str(i)
    c.execute('''
        INSERT INTO autori
        (id, jmeno, prijmeni)
        VALUES (?, ?, ?)
    ''',
    (i, jmeno, prijmeni))

for i in range(10):
    nazev = 'Clanek ' + str(i)
    obsah = 'Obsah ' + str(i)
    autor = i // 2
    c.execute(
        '''
            INSERT INTO clanky
            (nazev, obsah, autor)
            VALUES (?, ?, ?)
        ''',
        (nazev, obsah, autor)
    )

c.execute('''
    UPDATE clanky SET
        nazev = 'O Budulínkovi',
        obsah = 'Bylo nebylo...'
    WHERE id = 1
''')

c.execute('''
    UPDATE clanky SET
        nazev = nazev || '!!!'
''')

c.execute('''
    DELETE FROM clanky
    WHERE id = 4
''')

r = c.execute('''
    SELECT id, nazev, obsah, autor FROM clanky
    WHERE id < 6 AND nazev > 'Clanek 1'
''')

for cislo, nazev, obsah, autor in r:
    print(cislo, nazev, obsah, autor)

r = c.execute('''
    SELECT clanky.id, clanky.nazev, clanky.obsah,
        autori.jmeno, autori.prijmeni
    FROM clanky
    LEFT JOIN autori ON (autori.id == clanky.autor)
''')

for cislo, nazev, obsah, jmeno, prijmeni in r:
    print(cislo, nazev, obsah, jmeno, prijmeni)

