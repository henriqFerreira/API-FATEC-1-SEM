import sqlite3
import json

class db:
    def create_db(self):
        conn = sqlite3.connect("data.sqlite")

        with open("schema.sql") as f:
            conn.executescript(f.read())
    
    def insert_data(self, arquivo):
        conn = sqlite3.connect("data.sqlite")
        cur = conn.cursor()

        with open(arquivo, mode='r', encoding='utf-8') as f:
            content = json.load(f)
        for data in content:
            if "beneficios" in data and "descEmpresa" in data:
                cur.execute("INSERT INTO vagas (vaga_focada, vaga_categoria, vaga_titulo, vaga_nivel, vaga_empresa, vaga_salario, vaga_localizacao, vaga_descricao, vaga_beneficios, vaga_descricao_empresa) VALUES (?,?,?,?,?,?,?,?,?,?)", (data['focada'], data['categoria'], data['titulo'], data['nivel'], data['empresa'], data['salario'], data['localizacao'], data['descricao'], data['beneficios'], data['descEmpresa']))
                conn.commit()
            elif "beneficios" in data:
                cur.execute("INSERT INTO vagas (vaga_focada, vaga_categoria, vaga_titulo, vaga_nivel, vaga_empresa, vaga_salario, vaga_localizacao, vaga_descricao, vaga_beneficios) VALUES (?,?,?,?,?,?,?,?,?)", (data['focada'], data['categoria'], data['titulo'], data['nivel'], data['empresa'], data['salario'], data['localizacao'], data['descricao'], data['beneficios']))
                conn.commit()
            elif "descEmpresa" in data:
                cur.execute("INSERT INTO vagas (vaga_focada, vaga_categoria, vaga_titulo, vaga_nivel, vaga_empresa, vaga_salario, vaga_localizacao, vaga_descricao, vaga_descricao_empresa) VALUES (?,?,?,?,?,?,?,?,?)", (data['focada'], data['categoria'], data['titulo'], data['nivel'], data['empresa'], data['salario'], data['localizacao'], data['descricao'], data['descEmpresa']))
                conn.commit()
            else:
                cur.execute("INSERT INTO vagas (vaga_focada, vaga_categoria, vaga_titulo, vaga_nivel, vaga_empresa, vaga_salario, vaga_localizacao, vaga_descricao) VALUES (?,?,?,?,?,?,?,?)", (data['focada'], data['categoria'], data['titulo'], data['nivel'], data['empresa'], data['salario'], data['localizacao'], data['descricao']))
    
    def get_data_grafico(self):
        conn = sqlite3.connect("data.sqlite")
        cur = conn.cursor()


        stmt = cur.execute("SELECT COUNT(*) FROM vagas").fetchone()
        totalVagas = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=1").fetchone()
        vagasTi = stmt[0]
        stmt = cur.execute("SELECT COUNT(*) FROM vagas WHERE vaga_focada=0").fetchone()
        vagasGerais = stmt[0]

        data = {
            "totalVagas": totalVagas,
            "vagasTi": vagasTi,
            "vagasGerais": vagasGerais,
        }

        return data


