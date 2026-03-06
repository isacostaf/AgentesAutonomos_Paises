# biblioteca p python fazer requisicoes http
# permitir q ele acesse a internet
# Isso é como se o Python estivesse abrindo o site em segundo plano.
import requests

# ler e entender coisas no html
# O BeautifulSoup ajuda o Python a encontrar coisas dentro desse HTML. como titulo, nome, tabela..
from bs4 import BeautifulSoup

# criar funcao do agente
# funcao: coletar dados dos advogados
def coletar_paises():

    # criamos lista vazia chamada insights pra guardar
    insight = []

    # definimos o site q vai ser visitado
    # site para teste de programacao
    url = "https://www.worldometers.info/geography/alphabetical-list-of-countries/"

    # request.get faz uma requisicao de get
    # va ate esse site e baixe essa pagina
    # guardamos tudo em resposta
    # reposta vai ter o html da pagina (<head><title>titulo</title><head>),
    # status da pagina tbm 200,400...
    resposta = requests.get(url, verify=False)

    # ttranforma o html bruto em algo navegavel
    # <title>Example Domain</title>
    # soup eh onde ta guardado toda a estrutura da pagina
    soup = BeautifulSoup(resposta.text, "html.parser")

    # dentro de soup ache o title e pegue o texto dentro dela - e imprima
    # so pra testar se o scrapping funciona

    linhas = soup.find_all("tr")

    for i in linhas:

        # pegar as colunas so dessa linha por isso i
        colunas = i.find_all("td")

        if len(colunas) >= 3:

            pais = colunas[1].text
            populacao = colunas[2].text

            insight.append({
                "pais": pais,
                "populacao": populacao
            })
            
    return insight