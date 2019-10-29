import os
import webbrowser
import file_operations as fo
from offer import Offer

with open ('applied.txt', 'r') as file:
	for line in file:
		applied_count=int(line)

active_links=fo.create_list_old_links()
seen_links=fo.create_list_seen_links()

for link in active_links[:]:
	print("Offer: " + link)
	input("Open in browser. Press Enter.\n")
	webbrowser.open_new(link)
	try:
		applied=input("Applied? Press y/n")
		if applied[0] == 'y':
			applied_count += 1
			print('You have applied for: ' + str(applied_count) + ' jobs.\n')	
	
	except:
		continue
	seen_links.append(link)
	active_links.remove(link)

with open ('applied.txt', 'w') as file:
	file.write(str(applied_count))

with open ('seen_links.txt', 'a') as file:
	for line in seen_links:
		file.write(line)
os.remove('list_of_jobs.txt')

