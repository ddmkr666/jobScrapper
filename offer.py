import os
script_dir = os.path.dirname(__file__)

class Offer():
    def __init__(self, description, link):
        self.description = description
        self.link = link

    def __repr__(self):
        return str(self.description) + ',' + str(self.link)

    def save_to_file(self):
        seen_links = open(os.path.join(script_dir, 'files/seen_links.txt')).read().splitlines()
        old_links = open(os.path.join(script_dir, 'files/list_of_jobs.txt')).read().splitlines()
        if self.link not in seen_links + old_links:
            with open(os.path.join(script_dir, 'files/list_of_jobs.txt'), 'a', encoding='utf8') as file:
                file.write(self.__repr__() + '\n')
