import requests
from bs4 import BeautifulSoup
import json
import time

url = 'https://python-programs.com'
class_name = 'post-content'

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')
div = soup.find('div', {'class': class_name})

# Retry up to 5 times if the request fails
for retry in range(5):
    try:
        ul = div.ul
    except AttributeError:
        print(f'Retry {retry+1}: Request failed. Trying again in 5 seconds...')
        time.sleep(5)
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        div = soup.find('div', {'class': class_name})
    else:
        break
else:
    print('Failed to retrieve links after 5 retries. Exiting...')
    exit()

links = []
for li in ul.find_all('li'):
    link = li.a['href']
    links.append(link)

with open('links3.json', 'w') as f:
    json.dump(links, f)
