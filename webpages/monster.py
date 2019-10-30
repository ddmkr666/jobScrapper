'''
monster.it scrapper for new jobs containing 'linux'
'''
from offer import Offer
from bs4 import BeautifulSoup
import requests

def scrap_linux_bologna():
    # retrieve links to all recent offers in Bologna + 30km related to 'linux'
    r = requests.get("https://www.monster.it/lavoro/cerca/?q=linux&where=Bologna__2C-Emilia-Romagna&client=classic&cy=it&rad=30&intcid=swoop_Hero_Search")
    soup = BeautifulSoup(r.content, 'html.parser')
    for a in soup.findAll('div', attrs={'class':'summary'}):
        name = (a.find('a',href=True))
        description = str(name.contents)[2:-6:].title()
        link = name['href']
        Offer(description, link).save_to_file()
        
def scrap_linux_milan():
    # retrieve links to all recent offers in Milan + 30km related to 'linux'
    r = requests.get("https://www.monster.it/lavoro/cerca/?q=Linux&where=Milano__2C-Lombardia&client=classic&cy=it&rad=40&intcid=swoop_Hero_Search")
    soup = BeautifulSoup(r.content, 'html.parser')
    for a in soup.findAll('div', attrs={'class':'summary'}):
        name = (a.find('a',href=True))
        description = str(name.contents)[2:-6:].title()
        link = name['href']
        Offer(description, link).save_to_file()