'''
indeed.it scrapper for new jobs containing 'linux'
'''
from offer import Offer
from bs4 import BeautifulSoup
import requests

def scrap_linux_bologna():
    # retrieve links to all recent offers in Bologna + 30km related to 'linux'
    r = requests.get("https://it.indeed.com/offerte-lavoro?q=linux&l=Bologna%2C+Emilia-Romagna&sort=date")
    soup = BeautifulSoup(r.content, 'html.parser')
    for a in soup.select('a[onmousedown*="rclk(this,jobmap"]'):
        link = "https://www.indeed.com" + a['href']
        Offer(link).save_to_file()

def scrap_linux_milan():
    # retrieve links to all recent offers in Milan + 30km related to 'linux'
    r = requests.get("https://it.indeed.com/offerte-lavoro?q=linux&l=Milano%2C+Lombardia&sort=date")
    soup = BeautifulSoup(r.content, 'html.parser')
    for a in soup.select('a[onmousedown*="rclk(this,jobmap"]'):
        link = "https://www.indeed.com" + a['href']
        Offer(link).save_to_file()
        