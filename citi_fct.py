import json
from random import randrange

class brain:

    def __init__(self):

        self.score = 0
        self.bscore = 0
        self.route = []
        self.citi_data = []
        self.path = []
    
    def load_cities_data(self):
        with open('json/cities.json') as json_file:
            data = json.load(json_file)
        for each in data:
            citie = each['slug'] + ' (' + each['department_code'] + ')'
            self.citi_data.append(citie)

    def get_random_citie(self):
        r = randrange(len(self.citi_data))
        return self.citi_data[r]
    
    def add_path(self, citi):
        self.path.append(citi)

# b = brain()
# b.load_cities_data()
# print(b.get_random_citie())