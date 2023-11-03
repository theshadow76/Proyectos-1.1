from bs4 import BeautifulSoup
import requests
import time

def solotodo():
    link1 = requests.get('https://www.solotodo.cl/video_cards')
    soup = BeautifulSoup(link1, 'lxml')
    videocards_solotodo = soup.find_all('div', class_ = 'card-block d-flex justify-content-between flex-wrap category-browse-results')
    for vc in videocards_solotodo:
        vc_solotodo = vc.find('div', class_ = 'd-flex flex-column category-browse-result')
        name = vc.find('h3', class_ = 'h3')
        print(vc_solotodo)
