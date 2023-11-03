from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import selenium
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome('E:\coding\Shadow Tech Software 2\chromedriver\chromedriver\chromedriver 96\chromedriver.exe')

link1 = driver.get("https://www.solotodo.cl/video_cards")
link1_rq = requests.get("https://www.solotodo.cl/video_cards")
soup = BeautifulSoup(link1_rq, 'lxml')

gpu1 = soup.find_all('div', class_ = 'card-block d-flex justify-content-between flex-wrap category-browse-results').text
print(gpu1)

