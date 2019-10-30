import os
import webbrowser
import csv
#from offer import Offer

script_dir = os.path.dirname(__file__)
applied_count = open('applied.txt', 'r').read()

#seen_links = open(os.path.join(script_dir, 'files/seen_links.txt')).read().splitlines()
#active_links = open(os.path.join(script_dir, 'files/list_of_jobs.txt')).read().splitlines()

active_links=[]
with open(os.path.join(script_dir, 'files/list_of_jobs.txt'), 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        active_links.append(row)
csvFile.close()


for link in active_links:
    print("Offer: " + link[0])
    input("Open in browser. Press Enter.\n")
    webbrowser.open_new(link[1])
# 	try:
# 		applied=input("Applied? Press y/n")
# 		if applied[0] == 'y':
# 			applied_count += 1
# 			print('You have applied for: ' + str(applied_count) + ' jobs.\n')
#
# 	except:
# 		continue
# 	seen_links.append(link)
# 	active_links.remove(link)
#
# with open ('applied.txt', 'w') as file:
# 	file.write(str(applied_count))
#
# with open ('seen_links.txt', 'a') as file:
# 	for line in seen_links:
# 		file.write(line)
# os.remove('list_of_jobs.txt')

