from bs4 import BeautifulSoup as bs
import re

# Coleta o tweet e o autor
def coleta_tweets(html):
    arquivo = bs(html)

    # Pega todas as informações dentro de tags <section>
    fonte = arquivo.find_all('section')
    texto = "{a}".format(a = fonte[0]) # Trata o texto como string

    # Junta o termo em negrito com o resto do tweet
    texto = texto.replace('<span class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">', '')
    texto = texto.replace('</span>', '')
    texto = texto.replace('<span class="css-901oao css-16my406 r-1qd0xha r-vw2c0b r-ad9z0x r-bcqeeo r-qvutc0">', '')

    # Separa o texto em tags e conteúdos
    texto = texto.replace(">", ">\n").replace("<", "\n<")
    #print(texto)
    texto = texto.split("\n")

    # Insere o conteúdo numa lista
    lista = []
    for i in texto:
        if not(i.startswith("<") and i.endswith(">")) and not(i == ""):
            lista.append(i)

    return lista

# salvar ----->  '·''·'

def filtra_tweets(lista):
    tweet_individual = []
    lista_filtrada = []
    for i in range(len(lista)):
        tweet_individual = []
        if lista[i] == '·':
            aux = i+1
            #tweet_individual.append(lista[i-2])
            tweet_individual.append(lista[i-1])
            while aux + 3 < len(lista) and not(lista[aux + 3] == '·'):
                tweet_individual.append(lista[aux])
                aux += 1
                if aux + 3 == len(lista):
                    tweet_individual.append(lista[aux])
                    tweet_individual.append(lista[aux + 1])
                    tweet_individual.append(lista[aux + 2])
            lista_filtrada.append(tweet_individual)
    return lista_filtrada

def coleta_id(html):
    arquivo = bs(html)
    lista_aux = []
    lista_id = []

    fonte = arquivo.find_all('section')
    texto = "{a}".format(a = fonte[0])

    texto = texto.split(" ")

    for i in texto:
        if i.startswith("href="):
            lista_aux.append(i)

    for i in lista_aux:
        if not(("status" in i)) or (i.endswith('people"')):
            lista_aux.remove(i)

    for i in range(len(lista_aux) - 1):
        if not(lista_aux[i] == lista_aux[i + 1]):
            lista_id.append(lista_aux[i])

    for i in lista_id:
        if not('status' in i):
            lista_id.remove(i)

    return lista_id

def filtra_id(lista_id):
    lista_id_filtrada = []
    for i in lista_id:
        if not("photo" in i):
            for a in i.replace('"', '').split('/'):
                try:
                    int(a)
                    lista_id_filtrada.append(a)
                except:
                    pass
    return lista_id_filtrada

#def separa_tweets(lista):
#    lista_final = []
#    for i in range(len(lista)):
#        for aux in range(len(lista[i])):
#            lista_aux=[]
#            if lista[i][aux].startswith("@") and not(lista[i][aux + 3] == "Replying to "):
#                lista_aux.append(lista[i][aux])
#                lista_aux.append
