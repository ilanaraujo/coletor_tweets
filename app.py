# Funções do Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Usada pro sistema dar o sleep
import time

# Funções do outro arquivo
from coleta import *

# Webdriver
wd = webdriver.Chrome("./chromedriver")

# Dicionário com o número de dias de cada mês em 2020 (Fev. com 29 dias)
dias_mes = {
    1 : 31,
    2 : 29,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10: 31,
    11: 30,
    12: 31
    }

#lista_completa = []

# Pesquisa teste
wd.get("https://twitter.com/search?q=ufrj%20cloroquina%20lang%3Apt%20since%3A2019-12-01%20until%3A2020-10-01&src=typed_query&f=live")
time.sleep(5)
#Realiza o Scroll da página
while wd.execute_script("window.scrollTo(0,document.body.scrollHeight)"):
    wd.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
time.sleep(3)
html = wd.page_source
lista_tweet = coleta_tweets(html)
lista_tweet = filtra_tweets(lista_tweet)
lista_id = coleta_id(html)
lista_id = filtra_id(lista_id)
#lista_dia = filtra_tweets(coleta_tweets(html))
#lista_completa.append(lista_dia)
# Lista com as ids dos tweets
#lista_id_2 = filtra_id(lista_id)

print(len(lista_id),"IDs coletadas")
print(len(lista_tweet),"Tweets coletados")

for i in range(len(lista_id)):
    lista_tweet[i].insert(0, lista_tweet[i])

for i in lista_tweet:
    print(i)
