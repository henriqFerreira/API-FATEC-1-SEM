from flask import Flask, render_template, request, session, url_for, redirect
from django.core.paginator import Paginator
from flask_session import Session
from datetime import timedelta
from os.path import exists
from db import db
import sqlite3

app = Flask(__name__)
app.secret_key = 'binariosmelhorgrupo'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

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
            stmt2 = cur.execute("SELECT COUNT(*) FROM cursos").fetchone()[0]

            if stmt <= 0 and stmt2 <= 0:
                dados_vagas = ["./web-crawler/vagas-ti/vagas-ti.json", "./web-crawler/vagas-geral/vagas-geral.json"]
                for d in dados_vagas:
                    datab.insert_vagas(d)
                datab.insert_cursos("./web-crawler/cursos/cursos.json")
        else:
            datab.create_db()
            dados_vagas = ["./web-crawler/vagas-ti/vagas-ti.json", "./web-crawler/vagas-geral/vagas-geral.json"]
            for d in dados_vagas:
                datab.insert_vagas(d)
            datab.insert_cursos("./web-crawler/cursos/cursos.json")

@app.before_first_request
def inicializar():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)
    cx = Conexao("data")
    cx.verificarDB()
    return "Inicializando..."
    
@app.route("/")
def home():
    cx = Conexao("data")
    conn = cx.conectarBD()
    cur = conn.cursor()

    sessao = session.get('usuario')
    stmt2 = cur.execute("SELECT user_name FROM usuarios WHERE user_email = ?", (sessao,)).fetchone()
    
    if session.get('usuario') is not None:
        return render_template("home.html", sessao=stmt2['user_name'])
    else:
        return render_template("home.html", sessao=None)


@app.route("/cursos")
def cursos():
    cx = Conexao("data")
    conn = cx.conectarBD()
    cur = conn.cursor()

    sessao = session.get('usuario')
    stmt2 = cur.execute("SELECT user_name FROM usuarios WHERE user_email = ?", (sessao,)).fetchone()

    stmt = cur.execute("SELECT * FROM cursos ORDER BY RANDOM()").fetchall()
    conn.commit()
    
    try:
        page_num = int(request.args.get('page', 1))
    except:
        page_num = 1

    paginator = Paginator(stmt, 10)
    objects = list(paginator.get_page(page_num))
    obj = paginator.get_page(page_num)

    if session.get('usuario') is not None:
        return render_template("cursos.html", data=objects, obj=obj, sessao=stmt2['user_name'])
    else:
        return render_template("cursos.html", data=objects, obj=obj, sessao=None)

@app.route("/vagas")
def vagas():
    cx = Conexao("data")
    conn = cx.conectarBD()
    cur = conn.cursor()

    sessao = session.get('usuario')
    stmt2 = cur.execute("SELECT user_name FROM usuarios WHERE user_email = ?", (sessao,)).fetchone()

    stmt = cur.execute("SELECT * FROM vagas WHERE vaga_focada=1 ORDER BY RANDOM()").fetchall()
    conn.commit()
    
    try:
        page_num = int(request.args.get('page', 1))
    except:
        page_num = 1

    paginator = Paginator(stmt, 10)
    objects = list(paginator.get_page(page_num))
    obj = paginator.get_page(page_num)

    if session.get('usuario') is not None:
        return render_template('vagas.html', data=objects, obj=obj, sessao=stmt2['user_name'])
    else:
        return render_template('vagas.html', data=objects, obj=obj, sessao=None)

@app.route('/vagas/<categoria>')
def categoria(categoria):
    cx = Conexao("data")
    conn = cx.conectarBD()
    cur = conn.cursor()

    sessao = session.get('usuario')
    stmt2 = cur.execute("SELECT user_name FROM usuarios WHERE user_email = ?", (sessao,)).fetchone()

    categoriaStr = "%"+categoria+"%"
    stmt = cur.execute("SELECT * FROM vagas WHERE vaga_categoria LIKE (?) ORDER BY RANDOM();", [categoriaStr]).fetchall()
    conn.commit()
    
    try:
        page_num = int(request.args.get('page', 1))
    except:
        page_num = 1

    paginator = Paginator(stmt, 10)
    objects = list(paginator.get_page(page_num))
    obj = paginator.get_page(page_num)

    if session.get('usuario') is not None:
        return render_template('categoria.html', data=objects, obj=obj, categoria=categoria, sessao=stmt2['user_name'])
    else:
        return render_template('categoria.html', data=objects, obj=obj, categoria=categoria, sessao=None)


@app.route('/vaga_especifica/<vaga_id>')
def idVagas(vaga_id):
    cx = Conexao("data")
    conn = cx.conectarBD()
    cur = conn.cursor()

    sessao = session.get('usuario')
    stmt2 = cur.execute("SELECT user_name FROM usuarios WHERE user_email = ?", (sessao,)).fetchone()

    vaga_id= int(vaga_id)
    stmt = cur.execute("SELECT * FROM vagas WHERE vaga_id = (?);", (vaga_id,)).fetchone()
    conn.commit()

    if session.get('usuario') is not None:
        return render_template("vaga_especifica.html", stmt=stmt, sessao=stmt2['user_name'])
    else:
        return render_template("vaga_especifica.html", stmt=stmt, sessao=None)

@app.route("/contato")
def contato():
    cx = Conexao("data")
    conn = cx.conectarBD()
    cur = conn.cursor()

    sessao = session.get('usuario')
    stmt2 = cur.execute("SELECT user_name FROM usuarios WHERE user_email = ?", (sessao,)).fetchone()

    if session.get('usuario') is not None:
        return render_template("contato.html", sessao=stmt2['user_name'])
    else:
        return render_template("contato.html", sessao=None)

@app.route("/obrigado")
def obrigado():
    cx = Conexao("data")
    conn = cx.conectarBD()
    cur = conn.cursor()

    sessao = session.get('usuario')
    stmt2 = cur.execute("SELECT user_name FROM usuarios WHERE user_email = ?", (sessao,)).fetchone()

    if session.get('usuario') is not None:
        return render_template("obrigado.html", sessao=stmt2['user_name'])
    else:
        return render_template("obrigado.html", sessao=None)

@app.route("/institucional")
def institucional():
    cx = Conexao("data")
    conn = cx.conectarBD()
    cur = conn.cursor()

    sessao = session.get('usuario')
    stmt2 = cur.execute("SELECT user_name FROM usuarios WHERE user_email = ?", (sessao,)).fetchone()

    if session.get('usuario') is not None:
        return render_template("institucional.html", sessao=stmt2['user_name'])
    else:
        return render_template("institucional.html", sessao=None)

@app.route("/dados")
def dados():
    cx = Conexao("data")
    conn = cx.conectarBD()
    cur = conn.cursor()
    datab = db()
    dados = datab.get_data_grafico()

    sessao = session.get('usuario')
    stmt2 = cur.execute("SELECT user_name FROM usuarios WHERE user_email = ?", (sessao,)).fetchone()

    if session.get('usuario') is not None:
        return render_template("dados.html", data=dados, sessao=stmt2['user_name'])
    else:
        return render_template("dados.html", data=dados, sessao=None)

@app.route('/login')
def login():
    cx = Conexao("data")
    conn = cx.conectarBD()
    cur = conn.cursor()

    sessao = session.get('usuario')
    stmt2 = cur.execute("SELECT user_name FROM usuarios WHERE user_email = ?", (sessao,)).fetchone()

    if session.get('usuario') is not None:
        return redirect(url_for('home'))
    else:
        return render_template('login.html')

@app.route('/loginForm', methods=['POST'])
def loginForm():
    conn = Conexao("data")
    connected = conn.conectarBD()
    cur = connected.cursor()

    email = request.form['logEmail']
    senha = request.form['logSenha']

    stmt = cur.execute('SELECT * FROM usuarios WHERE user_email = ? AND user_senha = ? ', (email, senha)).fetchone()

    if stmt is None:
        return "Conta inexistente"
    else:
        session['usuario'] = email
        return redirect(url_for('home'))

@app.route("/register")
def register():
    cx = Conexao("data")
    conn = cx.conectarBD()
    cur = conn.cursor()

    sessao = session.get('usuario')
    stmt2 = cur.execute("SELECT user_name FROM usuarios WHERE user_email = ?", (sessao,)).fetchone()

    if session.get('usuario') is not None:
        return redirect(url_for('home'))
    else:
        return render_template('register.html')

@app.route("/registerForm", methods=['POST'])
def registerForm():
    conn = Conexao("data")
    connected = conn.conectarBD()
    cur = connected.cursor()

    nome = request.form['cadNome']
    email = request.form['cadEmail']
    senha = request.form['cadSenha']

    stmt = cur.execute('SELECT * FROM usuarios WHERE user_email = ?', (email,)).fetchone()

    if stmt is None:
        stmt2 = cur.execute('INSERT INTO usuarios (user_name, user_email, user_senha) VALUES (?,?,?)', (nome, email, senha))
        connected.commit()
        session['usuario'] = email
        return f"{session['usuario']}"
    else:
        return "E-mail já existente"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()