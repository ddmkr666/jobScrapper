'''
helplavoro.it scrapper for new jobs containing 'linux'
'''
from offer import Offer
from bs4 import BeautifulSoup
import requests

def scrap_linux_bologna():
    # retrieve links to all recent offers in Bologna + 30km related to 'linux'
    r = requests.get("https://www.helplavoro.it/ricerca/linux/in-provincia-di-bologna.html")
    soup = BeautifulSoup(r.content, 'html.parser')
    for a in soup.findAll('a', attrs={'class': 'posizione link-offerta'}):
        link = 'https://www.helplavoro.it' + a['href']
        Offer(link).save_to_file()
        
def scrap_linux_milan():
    # retrieve links to all recent offers in Milan + 30km related to 'linux'
    r = requests.get("https://www.helplavoro.it/ricerca/linux/in-provincia-di-milano.html")
    soup = BeautifulSoup(r.content, 'html.parser')
    for a in soup.findAll('a', attrs={'class':'posizione link-offerta'}):
        link = 'https://www.helplavoro.it' + a['href']
        Offer(link).save_to_file()
        