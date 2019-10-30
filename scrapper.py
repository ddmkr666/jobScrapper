'''
job scrapper
'''
import monster
import helplavoro
import jobrapido
import indeed

# retrieve all linux related jobs
open('list_of_jobs.txt', 'a').close()
monster.scrap_linux_bologna()
monster.scrap_linux_milan()
helplavoro.scrap_linux_bologna()
helplavoro.scrap_linux_milan()
jobrapido.scrap_linux_bologna()
jobrapido.scrap_linux_milan()
indeed.scrap_linux_bologna()
indeed.scrap_linux_milan()