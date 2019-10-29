class Offer():
    def __init__(self, description):
        self.description = description
        #self.link = link

    def __repr__(self):
        return str(self.description)

    def save_to_file(self):
        seen_links = open('seen_links.txt').read().splitlines()
        old_links = open('list_of_jobs.txt').read().splitlines()
        if self.description not in seen_links + old_links:
            with open('list_of_jobs.txt', 'a') as file:
                file.write(self.__repr__() + '\n')