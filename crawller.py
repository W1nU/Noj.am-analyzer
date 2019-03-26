import requests as r
from bs4 import BeautifulSoup as bs

class Crawller:
    def __init__(self):
        pass

    def create_bs_object(self, html):
        return bs(html, 'html.parser')

    def get_info_from_id(self, id):
        raw_html = r.get('https://www.acmicpc.net/user/' + id)
        bs = self.create_bs_object(raw_html.text)
        problems = list(map(lambda x : x.text, bs.find_all('span', {'class' : 'problem_number'})))
        
        return problems
    