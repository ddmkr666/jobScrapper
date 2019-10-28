import os

def create_list_old_links():
    old_links=[]
    with open('list_of_jobs.txt', 'r') as file:
        for line in file:
            old_links.append(line)
    return old_links

def save_new_offers_to_text_file():
    new_links=[]
    old_links=create_list_old_links()
    seen_links=create_list_seen_links()
    with open('monster_linux_daily.txt', 'r') as file:
        for line in file:
            new_links.append(line)

    with open('list_of_jobs.txt', 'a') as file:
        for line in new_links:
            if line not in old_links and line not in seen_links:
                file.write(line)

def cleanup_temporary_files():
    os.remove('monster_linux_daily.txt')

def create_list_seen_links():
    seen_links=[]
    with open ('seen_links.txt', 'r') as file:
        for line in file:
            seen_links.append(line)
    return seen_links