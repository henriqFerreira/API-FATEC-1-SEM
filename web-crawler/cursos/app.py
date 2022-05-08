import json
from nis import cat
from bs4 import BeautifulSoup
import requests

# Variáveis de tratamento de URL
url = "https://www.sebrae.com.br/sites/render/component?vgnextcomponentid=3263d864e639a610VgnVCM1000004c00210aRCRD&qtd=0&order=0&filters=&batchsize=290"

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
	# Raspagem do título dos cursos
	tituloCurso = htmlCursos.find('div', class_='sb-components__card__info__title').text
	tituloCurso = tituloCurso.split()
	tituloCurso = ' '.join(tituloCurso)

	# Raspagem da categoria dos cursos
	categoriaCurso = htmlCursos.find('div', class_='sb-components__card__info__tags').text
	categoriaCurso = categoriaCurso.split()
	categoriaCurso = ' '.join(categoriaCurso)
	categoriaCurso = categoriaCurso.split('/')
	categoriaCurso = categoriaCurso[1]

	# Raspagem da duração dos cursos
	if htmlCursos.find('span', class_='sb-components__card__info__details__icon ic1') is not None:
		duracaoCurso = htmlCursos.find('span', class_='sb-components__card__info__details__icon ic1').text
		duracaoCurso = duracaoCurso.split()
		duracaoCurso = ' '.join(duracaoCurso)
	else:
		duracaoCurso = None
	
	# Raspagem do tempo de conclusão dos cursos
	if htmlCursos.find('span', class_='sb-components__card__info__details__icon ic2') is not None:
		conclusaoCurso = htmlCursos.find('span', class_='sb-components__card__info__details__icon ic2').text
		conclusaoCurso = conclusaoCurso.split()
		conclusaoCurso = ' '.join(conclusaoCurso)
	else:
		conclusaoCurso = None

	dict_cursos.append({
		"tituloCurso": tituloCurso,
		"categoriaCurso": categoriaCurso,
		"tipoCurso": "Gratuito",
		"formatoCurso": "Online",
		"duracaoCurso": duracaoCurso,
		"conclusaoCurso": conclusaoCurso
	})

with open(arquivo, 'w', encoding='utf-8') as f:
  json.dump(dict_cursos, f, ensure_ascii=False, indent=4, separators=(',',': '))