import requests
from bs4 import BeautifulSoup   

URL = requests.get("https://www.exito.com/iphone-11-de-128gb-en-blanco-apple-mhdj3lza-3006616/p")
HEADER ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
page = requests.get(URL, headers = HEADER)
soup = BeautifulSoup(page.content, "lxml")
print(soup.prettify())