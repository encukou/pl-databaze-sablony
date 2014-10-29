from jinja2 import Template
import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def seznam_clanku():
    with open('sablona.txt') as f:
        sablona = Template(
            f.read(),
            autoescape=True)

    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    clanky = c.execute('''
        SELECT clanky.nazev, clanky.obsah, autori.jmeno, autori.prijmeni
        FROM clanky
        LEFT JOIN autori ON (autori.id == clanky.autor)
    ''')

    vystup = sablona.render(clanky=clanky)

    return vystup

if __name__ == '__main__':
    app.run(debug=True, port=8000)
