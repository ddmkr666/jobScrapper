'''
job scrapper
'''
import monster
import os
import file_operations as fo

# retrieve all linux related jobs
open('list_of_jobs.txt', 'a').close()
monster.scrap_linux_bologna()
monster.scrap_linux_milan()

# save to file and cleanup
fo.save_new_offers_to_text_file()
fo.cleanup_temporary_files()
