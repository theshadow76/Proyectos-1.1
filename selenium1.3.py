from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import selenium
from selenium.webdriver.firefox.options import Options as FirefoxOptions

op = Options()
#disable JavaScript
op.set_preference('javascript.enabled', True)

driver = webdriver.Firefox(executable_path= 'E:\\coding\\Shadow Tech Software 2\\geckodriver\\ultime driver\\geckodriver.exe')

link1 = driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Des-419%26next%3D%252F&hl=es-419&passive=false&service=youtube&uilel=0&flowName=GlifWebSignIn&flowEntry=AddSession')

inp1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")))
inp1.click()
inp1.send_keys("rickiwalker05@gmail.com")

btn1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")))
btn1.click()