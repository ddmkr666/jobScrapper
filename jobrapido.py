'''
jobrapido.it scrapper for new jobs containing 'linux'
'''
from offer import Offer
from bs4 import BeautifulSoup
import requests

def scrap_linux_bologna():
    # retrieve links to all recent offers in Bologna + 30km related to 'linux'
    r = requests.get("https://it.jobrapido.com/?&w=linux&l=bologna&r=45&shm=all&sortby=publish_date")
    soup = BeautifulSoup(r.content, 'html.parser')
    for a in soup.findAll('a', attrs={'class': 'advert-link'}):
        link = a['href']
        Offer(link).save_to_file()
        
def scrap_linux_milan():
    # retrieve links to all recent offers in Milan + 30km related to 'linux'
    r = requests.get("https://it.jobrapido.com/?&w=linux&l=milano&r=45&sortby=publish_date&shm=all")
    soup = BeautifulSoup(r.content, 'html.parser')
    for a in soup.findAll('a', attrs={'class': 'advert-link'}):
        link = a['href']
        Offer(link).save_to_file()
        