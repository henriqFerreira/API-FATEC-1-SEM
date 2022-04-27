import json
from bs4 import BeautifulSoup
import requests

contador = 0
limite = 1

# Variáveis de tratamento de URL
urlbase = "https://www.vagas.com.br/vagas-de-"
urlVaga = "https://www.vagas.com.br"
palavras_chaves = [
    "ti", "banco-de-dados", "redes", "software",
    "hardware", "matematica", "back-end", "front-end",
    "segurança-da-informação", "engenheiro-de-dados", "administração",
    "cientista-de-dados"
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
      dictionary[key] = value.strip()

for palavra in palavras_chaves:
    urlContent = requests.get(urlbase+palavra).content
    interpretedHtml = BeautifulSoup(urlContent, 'html.parser')

    for htmlVagas in interpretedHtml.find_all('li', class_='vaga odd')[:int(limite)]:
        contador += 1

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
                  "id": f"{contador}",
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
                  "id": f"{contador}",
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
                  "id": f"{contador}",
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
                  "id": f"{contador}",
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