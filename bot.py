from requests_html import HTMLSession
from bs4 import BeautifulSoup
import argparse
import pandas as pd
import webs3
s=HTMLSession()

my_parser=argparse.ArgumentParser(description='Busca una keywords en amazon y la scrapea')
my_parser.add_argument('searchterm',metavar='searchterm',type=str,help='Utiliza + para espacios')
args=my_parser.parse_args()
searchterm=args.searchterm

url=f'https://www.amazon.es/s?k={searchterm}&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss'

def get_data(url):
	r=s.get(url)
	r.html.render(timeout=20)
	soup=BeautifulSoup(r.html.html,'html.parser')

	return soup



def get_object(soup):
	products=soup.find_all('div',{'data-component-type':'s-search-result'})
	lista_diccionarios=[]
	for product in products:
		title=product.find('a',{'class':'a-link-normal a-text-normal'}).text[:25]
		link='https://www.amazon.es'+product.find('a',{'class':'a-link-normal a-text-normal'})['href']
		try:
			price=product.find('span',{'class':'a-price-whole'}).text
		except:
			price=0
		try:
			reviews=int(product.find('span',{'class':'a-size-base'}).text)
		except:
			reviews=0

		almacenador={
		'title':title,
		'link':link,
		'price':price,
		'reviews':reviews
		}

		lista_diccionarios.append(almacenador)
	return lista_diccionarios

lista_paginas=webs3.pagination(url)
contador=1
for pagina in lista_paginas:
	df=pd.DataFrame(get_object(get_data(pagina)))
	df.to_csv(searchterm+'numero'+str(contador)+'.csv')
	contador += 1