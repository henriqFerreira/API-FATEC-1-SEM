from flask import Flask, render_template
import sqlite3
from db import db

app = Flask("__name__")

class Conexao(db):
    def __init__(self, bancoDeDados):
        self.bd = bancoDeDados

    def conectarBD(self):
        db = db()
        db.create_db()
        conn = sqlite3.connect(self.bd+".sqlite")
        return conn

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cursos")
def cursos():
    return render_template("cursos.html")

@app.route("/vagas")
def vagas():
    return render_template("vagas.html")

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