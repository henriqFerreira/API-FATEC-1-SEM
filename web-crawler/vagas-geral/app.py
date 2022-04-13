import json
from bs4 import BeautifulSoup
import requests

contador = 0

# Variáveis de tratamento de URL
urlbase = "https://www.vagas.com.br/vagas-de-"
palavras_chaves = [
    "engenharia", "piloto", "professor", "vendedor",
    "advogado", "manufatura", "médico", "químico", 
]
# Variável de armazenamento de um 'dicionário' de vagas
dict_vagas = []

# Arquivo JSON que armazenará cada vaga
arquivo = "./vagas-geral/vagas-geral.json"

def remove(dictionary):
  for key, value in dictionary.items():
    if isinstance(value, dict):
      remove(value)
    else:
      dictionary[key] = value.strip()

for palavra in palavras_chaves:
    urlContent = requests.get(urlbase+palavra).content
    interpretedHtml = BeautifulSoup(urlContent, 'html.parser')

    for htmlVagas in interpretedHtml.find_all('li', class_='vaga odd')[:5]:
        contador += 1

        tituloVaga = htmlVagas.find('a', class_='link-detalhes-vaga').text
        empresaVaga = htmlVagas.find('span', class_='emprVaga').text
        nivelVaga = htmlVagas.find('span', class_='nivelVaga').text
        descricaoVaga = htmlVagas.find('div', class_='detalhes').text
        localizacaoVaga = htmlVagas.find('span', class_='vaga-local').text

        dict_vagas.append({
            "id": f"{contador}",
            "categoria": palavra,
            "titulo": tituloVaga,
            "salario": "À combinar",
            "empresa": empresaVaga,
            "nivel": nivelVaga,
            "descricao": descricaoVaga,
            "localizacao": localizacaoVaga
            })

with open(arquivo, mode='r', encoding='utf-8') as loadJson:
    data = json.load(loadJson)

for dataToInsert in dict_vagas:
    remove(dataToInsert)
    data.append(dataToInsert)

with open(arquivo, mode='w', encoding='utf-8') as newData:
    json.dump(data, newData, ensure_ascii=False, indent=4, separators=(',',': '))
