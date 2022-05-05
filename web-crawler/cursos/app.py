import json
from bs4 import BeautifulSoup
import requests

# Variáveis de tratamento de URL
url = "https://www.sebrae.com.br/sites/PortalSebrae/cursosonline"

# Variável de armazenamento de um 'dicionário' de vagas
dict_cursos = []

# Arquivo JSON que armazenará cada vaga
arquivo = "./web-crawler/cursos/cursos.json"

def remove(dictionary):
	for key, value in dictionary.items():
		if isinstance(value, dict):
			remove(value)
		else:
			dictionary[key] = value.strip()

urlContent = requests.get(url).content
interpretedHtml = BeautifulSoup(urlContent, 'html.parser')
cursosContent = interpretedHtml.find('div', class_='sb-home-ead__learn-today__cards')

for htmlCursos in cursosContent.find_all('div', class_='sb-components__card'):
	tituloCurso = htmlCursos.find('div', class_='sb-components__card__info__title').text
	print(tituloCurso)

	# dict_cursos.append({
	# 		"titulo": format_mesage(tituloCurso),
	# 		"descricao": format_mesage(descricaoCurso),
	# 		})

# with open(arquivo, 'w', encoding='utf-8') as f:
#   json.dump(dict_cursos, f, ensure_ascii=False, indent=4, separators=(',',': '))