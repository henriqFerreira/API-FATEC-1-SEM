from flask import Flask, render_template
import sqlite3
from os.path import exists
from db import db

app = Flask(__name__)

class Conexao(db):
    def __init__(self, bancoDeDados):
        self.bancoDeDados = bancoDeDados

    def conectarBD(self):
        conn = sqlite3.connect(self.bancoDeDados+".sqlite")
        conn.row_factory = sqlite3.Row
        return conn
    
    def verificarDB(self):
        cx = Conexao("data")
        datab = db()

        if exists(self.bancoDeDados+".sqlite"):
            conn = cx.conectarBD()
            cur = conn.cursor()
            stmt = cur.execute("SELECT COUNT(*) FROM vagas").fetchone()[0]

            if stmt <= 0:
                datab.insert_data("./web-crawler/vagas-ti/vagas-ti.json")
        else:
            datab.create_db()
            datab.insert_data("./web-crawler/vagas-ti/vagas-ti.json")

@app.before_first_request
def inicializar():
    cx = Conexao("data")
    cx.verificarDB()
    return "Inicializando..."
    
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cursos")
def cursos():
    return render_template("cursos.html")

@app.route("/vagas")
def vagas():
    cx = Conexao("data")
    conn = cx.conectarBD()
    cur = conn.cursor()

    stmt = cur.execute("SELECT * FROM vagas").fetchall()
    conn.commit()

    return render_template("vagas.html", data=stmt)

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/institucional")
def institucional():
    return render_template("institucional.html")

@app.route("/dados")
def dados():
    return render_template("dados.html")

if __name__ == "__main__":
    app.run()