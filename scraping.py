#! /usr/local/bin/python3.7

from bs4 import BeautifulSoup
import csv
import requests

def exportBlagounette(blague, writer):
	assert blague != None;
	content = BeautifulSoup(blague, "html.parser");
	category = content.find('span', attrs={ 'itemprop' : 'name', 'class' : 'articlepostheadername'}).text
	blagounette = content.find('div', attrs={ 'class' : 'articlepostcorpsdiv', 'itemprop' : 'articleBody'}).text
	writer.writerow([category, blagounette])

page = requests.get('https://www.blague.lol/blague/')
content = BeautifulSoup(page.text, "html.parser").find_all('div', attrs={ 'itemtype' : 'http://schema.org/Article', 'class' : 'articlepost'})

with open('blagounette.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile)
	for blague in content:
		try:
			exportBlagounette(str(blague), writer);
		except AssertionError as e:
			print(e)