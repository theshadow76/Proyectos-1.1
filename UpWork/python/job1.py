import bs4
from bs4 import BeautifulSoup
import requests

File = open("out.csv", "a")

soup = BeautifulSoup

main = "https://comandoaudio.com/collections/subwoofer"

# first scrape
try:
    title = soup.find("div",
                          attrs={"class": 'product-list product-list--collection '})
    title_value = title.string
 
    title_string = title_value.strip().replace(',', '')
           
except AttributeError:
 
        title_string = "NA"
 
        print("product Title = ", title_string)

File.write(f"{title_string},")
File.close()


