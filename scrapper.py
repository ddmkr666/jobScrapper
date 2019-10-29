'''
job scrapper
'''
from offer import Offer
import monster
import os

# retrieve all linux related jobs
open('list_of_jobs.txt', 'a').close()
monster.scrap_linux_bologna()
monster.scrap_linux_milan()