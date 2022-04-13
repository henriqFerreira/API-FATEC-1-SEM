from encodings import utf_8
import json
from bs4 import BeautifulSoup
import requests

# Variáveis de tratamento de URL
urlbase = "https://www.cursosonlinebra.com.br/cursos/"
palavras_chaves = [
    "15/informatica-e-tecnologia-.html", "1/administracao-e-contabilidade-.html", "5/biologia-e-meio-ambiente-.html",
    "9/construcao-civil.html", "10/direito.html", "11/educacao-e-pedagogia.html", "13/educacao-fisica-e-estetica-.html",
    "16/linguagens.html", "18/marketing-e-seus-seguimentos.html", "19/musica.html", "20/nutricao-e-gastronomia-.html", 
    "23/politica.html", "odontologia-e-saude.html", "27/psicologia-.html"
]
# Variável de armazenamento de um 'dicionário' de vagas
dict_cursos = []

# Arquivo JSON que armazenará cada vaga
arquivo = "./cursos/cursos.json"

def remove(dictionary):
  for key, value in dictionary.items():
    if isinstance(value, dict):
      remove(value)
    else:
      dictionary[key] = value.strip()

def format_mesage (txt):
  txt = txt.replace(' ', '')
  txt = txt.replace('\n', '')
  return txt

for palavra in palavras_chaves:
    urlContent = requests.get(urlbase+palavra).content
    interpretedHtml = BeautifulSoup(urlContent, 'html.parser')

    for htmlCursos in interpretedHtml.find_all('div', class_='content col-md-6')[:3]:
        tituloCurso = htmlCursos.find('h6', class_='').text
        descricaoCurso = htmlCursos.find('p', class_='description').text

        dict_cursos.append({
             "titulo": format_mesage(tituloCurso),
             "descricao": format_mesage(descricaoCurso),
             })

with open(arquivo, 'w', encoding='utf-8') as f:
  json.dump(dict_cursos, f, ensure_ascii=False, indent=4, separators=(',',': '))