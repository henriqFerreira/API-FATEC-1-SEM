import json
from bs4 import BeautifulSoup
import requests

focada = True

# Variáveis de tratamento de URL
urlbase = "https://www.vagas.com.br/vagas-de-"
urlVaga = "https://www.vagas.com.br"
palavras_chaves = [
    "ti", "banco-de-dados", "redes", "software",
    "hardware", "back-end", "front-end", "segurança-da-informação",
    "engenheiro-de-dados", "cientista-de-dados", "programação", "desenvolvedor",
    "business-inteligence", "cloud-computing", "inteligência-artificial", "python",
    "php", "javaScript", "fullstack", "java", "web-designer", "sênior",
	"pleno", "dba", "sistemas", "SQL", "server", "informática", "tecnologia",
]
# Variável de armazenamento de um 'dicionário' de vagas
dict_vagas = []

# Arquivo JSON que armazenará cada vaga
arquivo = "./web-crawler/vagas-ti/vagas-ti.json"

def remove(dictionary):
	for key, value in dictionary.items():
		if isinstance(value, dict):
			remove(value)
		else:
			if isinstance(dictionary[key], str):
				dictionary[key] = value.strip()

for palavra in palavras_chaves:
    urlContent = requests.get(urlbase+palavra).content
    interpretedHtml = BeautifulSoup(urlContent, 'html.parser')

    for htmlVagas in interpretedHtml.select('li.vaga'):
        # Raspagem do título das vagas
        tituloVaga = htmlVagas.find('a', class_='link-detalhes-vaga').text
        tituloVaga = tituloVaga.split()
        tituloVaga = ' '.join(tituloVaga)

        # Raspagem da empresa das vagas
        empresaVaga = htmlVagas.find('span', class_='emprVaga').text
        empresaVaga = empresaVaga.split()
        empresaVaga = ' '.join(empresaVaga)

        # Raspagem do nível técnico das vagas
        nivelVaga = htmlVagas.find('span', class_='nivelVaga').text
        nivelVaga = nivelVaga.split()
        nivelVaga = ' '.join(nivelVaga)

        # Raspagem da localização das vagas
        if htmlVagas.find('span', class_='vaga-local') is not None:
            localizacaoVaga = htmlVagas.find('span', class_='vaga-local').text
            localizacaoVaga = localizacaoVaga.split()
            localizacaoVaga = ' '.join(localizacaoVaga)
            localizacaoVaga = localizacaoVaga.split("/")
            cidade = localizacaoVaga[0]
            if len(localizacaoVaga) > 1:
                estado = localizacaoVaga[1]
            else:
                estado = None
        else:
            cidade = None
            estado = None

        # Request da página de cada vaga
        vagaHref = htmlVagas.find('a', class_='link-detalhes-vaga', href=True)
        vagaInfo = requests.get(urlVaga+vagaHref['href']).content
        interpretedVagaInfo = BeautifulSoup(vagaInfo, 'html.parser')

        for info in interpretedVagaInfo.find_all('article', class_="vaga job-group"):
            # Raspagem da descrição das vagas
            descricaoVaga = info.find('div', class_="job-description__text").text
            descricaoVaga = descricaoVaga.split()
            descricaoVaga = ' '.join(descricaoVaga)

            if (info.find('ul', class_="job-benefits__list") and info.find('div', class_="job-company-presentation")):
                #   Raspagem dos benefícios das vaga
                beneficiosVaga = info.find('ul', class_="job-benefits__list").text
                beneficiosVaga = beneficiosVaga.split()
                beneficiosVaga = ' '.join(beneficiosVaga)

                # Raspagem da descrição da empresa das vagas
                descricaoEmpresa = info.find('div', class_="job-company-presentation").text
                descricaoEmpresa = descricaoEmpresa.split()
                descricaoEmpresa = ' '.join(descricaoEmpresa)

                dict_vagas.append({
                    "focada": focada,
                    "categoria": palavra,
                    "titulo": tituloVaga,
                    "salario": "À combinar",
                    "empresa": empresaVaga,
                    "nivel": nivelVaga,
                    "descricao": descricaoVaga,
                    "cidade": cidade,
                    "estado": estado,
                    "beneficios": beneficiosVaga,
                    "descEmpresa": descricaoEmpresa
                })
            elif (info.find('ul', class_="job-benefits__list")):
                #   Raspagem dos benefícios das vaga
                beneficiosVaga = info.find('ul', class_="job-benefits__list").text
                beneficiosVaga = beneficiosVaga.split()
                beneficiosVaga = ' '.join(beneficiosVaga)

                dict_vagas.append({
                    "focada": focada,
                    "categoria": palavra,
                    "titulo": tituloVaga,
                    "salario": "À combinar",
                    "empresa": empresaVaga,
                    "nivel": nivelVaga,
                    "descricao": descricaoVaga,
                    "cidade": cidade,
                    "estado": estado,
                    "beneficios": beneficiosVaga,
                })
            elif (info.find('div', class_="job-company-presentation")):
                # Raspagem da descrição da empresa das vagas
                descricaoEmpresa = info.find('div', class_="job-company-presentation").text
                descricaoEmpresa = descricaoEmpresa.split()
                descricaoEmpresa = ' '.join(descricaoEmpresa)

                dict_vagas.append({
                    "focada": focada,
                    "categoria": palavra,
                    "titulo": tituloVaga,
                    "salario": "À combinar",
                    "empresa": empresaVaga,
                    "nivel": nivelVaga,
                    "descricao": descricaoVaga,
                    "cidade": cidade,
                    "estado": estado,
                    "descEmpresa": descricaoEmpresa
                })
            else:
                dict_vagas.append({
                    "focada": focada,
                    "categoria": palavra,
                    "titulo": tituloVaga,
                    "salario": "À combinar",
                    "empresa": empresaVaga,
                    "nivel": nivelVaga,
                    "descricao": descricaoVaga,
                    "cidade": cidade,
                    "estado": estado,
                })

with open(arquivo, mode='r', encoding='utf-8') as loadJson:
    data = json.load(loadJson)

for dataToInsert in dict_vagas:
    remove(dataToInsert)
    data.append(dataToInsert)

with open(arquivo, mode='w', encoding='utf-8') as newData:
    json.dump(data, newData, ensure_ascii=False, indent=4, separators=(',',': '))