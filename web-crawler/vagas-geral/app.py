import json
from bs4 import BeautifulSoup
import requests

focada = False

# Variáveis de tratamento de URL
urlbase = "https://www.vagas.com.br/vagas-de-"
urlVaga = "https://www.vagas.com.br"
palavras_chaves = [
    "médico", "marceneiro", "geral", "ajudante", "dentista",
    "clínico", "vendedor", "transporte", "aprendiz", "soldador",
    "servente", "obras", "administrativo", "nutricionista", "eletricista",
    "confeiteiro", "operador", "cobrador", "almoxarifado", "vigilante", "designer",
    "químico", "administração", "mecânico", "logística", "segurança", "gerente",
    "manicure", "pedicure", "estoquista", "professor", "limpeza", "fiscal",
    "analista", "entregador", "motorista", "serralheiro", "suporte", "telemarketing",
    "frentista"
]
# Variável de armazenamento de um 'dicionário' de vagas
dict_vagas = []

# Arquivo JSON que armazenará cada vaga
arquivo = "./web-crawler/vagas-geral/vagas-geral.json"

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

    for htmlVagas in interpretedHtml.select('li.vaga')[:5]:

        tituloVaga = htmlVagas.find('a', class_='link-detalhes-vaga').text
        empresaVaga = htmlVagas.find('span', class_='emprVaga').text
        nivelVaga = htmlVagas.find('span', class_='nivelVaga').text
        localizacaoVaga = htmlVagas.find('span', class_='vaga-local').text

        vagaHref = htmlVagas.find('a', class_='link-detalhes-vaga', href=True)
        vagaInfo = requests.get(urlVaga+vagaHref['href']).content
        interpretedVagaInfo = BeautifulSoup(vagaInfo, 'html.parser')

        for info in interpretedVagaInfo.find_all('article', class_="vaga job-group"):
            descricaoVaga = info.find('div', class_="job-description__text").text

            if (info.find('ul', class_="job-benefits__list") and info.find('div', class_="job-company-presentation")):
              beneficiosVaga = info.find('ul', class_="job-benefits__list").text
              descricaoEmpresa = info.find('div', class_="job-company-presentation").text

              dict_vagas.append({
                  "focada": focada,
                  "categoria": palavra,
                  "titulo": tituloVaga,
                  "salario": "À combinar",
                  "empresa": empresaVaga,
                  "nivel": nivelVaga,
                  "descricao": descricaoVaga,
                  "localizacao": localizacaoVaga,
                  "beneficios": beneficiosVaga,
                  "descEmpresa": descricaoEmpresa
                  })
            elif (info.find('ul', class_="job-benefits__list")):
              beneficiosVaga = info.find('ul', class_="job-benefits__list").text

              dict_vagas.append({
                  "focada": focada,
                  "categoria": palavra,
                  "titulo": tituloVaga,
                  "salario": "À combinar",
                  "empresa": empresaVaga,
                  "nivel": nivelVaga,
                  "descricao": descricaoVaga,
                  "localizacao": localizacaoVaga,
                  "beneficios": beneficiosVaga,
              })
            elif (info.find('div', class_="job-company-presentation")):
              descricaoEmpresa = info.find('div', class_="job-company-presentation").text

              dict_vagas.append({
                  "focada": focada,
                  "categoria": palavra,
                  "titulo": tituloVaga,
                  "salario": "À combinar",
                  "empresa": empresaVaga,
                  "nivel": nivelVaga,
                  "descricao": descricaoVaga,
                  "localizacao": localizacaoVaga,
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
                  "localizacao": localizacaoVaga,
              })

with open(arquivo, mode='r', encoding='utf-8') as loadJson:
    data = json.load(loadJson)

for dataToInsert in dict_vagas:
    remove(dataToInsert)
    data.append(dataToInsert)

with open(arquivo, mode='w', encoding='utf-8') as newData:
    json.dump(data, newData, ensure_ascii=False, indent=4, separators=(',',': '))