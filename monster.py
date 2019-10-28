'''
monster.it scrapper for new jobs containing 'linux'
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

def scrap_linux_bologna():
    # retrieve links to all recent offers in Bologna + 30km related to 'linux'
    driver = webdriver.Chrome()
    content = driver.page_source
    r=requests.get("https://www.monster.it/lavoro/cerca/?q=linux&where=Bologna__2C-Emilia-Romagna&client=classic&cy=it&rad=30&intcid=swoop_Hero_Search")
    soup = BeautifulSoup(r.content, 'html.parser')
    for a in soup.findAll('div', attrs={'class':'summary'}):
        name=a.find('a',href=True)
        with open('monster_linux_daily.txt', 'a') as file:
            file.write(name['href'])
            file.write('\n')

def scrap_linux_milan():
    # retrieve links to all recent offers in Milan + 30km related to 'linux'
    driver = webdriver.Chrome()
    content = driver.page_source
    r=requests.get("https://www.monster.it/lavoro/cerca/?q=Linux&where=Milano__2C-Lombardia&client=classic&cy=it&rad=40&intcid=swoop_Hero_Search")
    soup = BeautifulSoup(r.content, 'html.parser')
    for a in soup.findAll('div', attrs={'class':'summary'}):
        name=a.find('a',href=True)
        with open('monster_linux_daily.txt', 'a') as file:
            file.write(name['href'])
            file.write('\n')
