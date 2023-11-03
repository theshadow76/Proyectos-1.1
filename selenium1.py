from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import selenium

driver = webdriver.Chrome('E:\coding\Shadow Tech Software 2\chromedriver\chromedriver\chromedriver 96\chromedriver.exe')

link1 = driver.get('https://www.tiktok.com/@vigo_walker/video/7019664881121037573?is_copy_url=1&is_from_webapp=v1')

whatch = True

while (whatch == True):
    time.sleep(1)
    driver.refresh()