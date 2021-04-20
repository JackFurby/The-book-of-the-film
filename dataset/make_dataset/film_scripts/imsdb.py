import requests
from bs4 import BeautifulSoup

headers = {
	'Access-Control-Allow-Origin': '*',
	'Access-Control-Allow-Methods': 'GET',
	'Access-Control-Allow-Headers': 'Content-Type',
	'Access-Control-Max-Age': '3600',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

url = "https://imsdb.com/all-scripts.html"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

links = soup.select('td p a')
'''
for i in links:
	req = requests.get("https://imsdb.com" + i['href'], headers)
	soup = BeautifulSoup(req.content, 'html.parser')
	pageLinks = soup.select('a')
	for i in pageLinks:
		if isinstance(i.string, str) and ("Read " in i.string):
			print(i['href'])
'''



req = requests.get("https://imsdb.com" + links[0]['href'], headers)
soup = BeautifulSoup(req.content, 'html.parser')
pageLinks = soup.select('a')
for i in pageLinks:
	if isinstance(i.string, str) and ("Read " in i.string):
		req = requests.get("https://imsdb.com" + i['href'], headers)
		soup = BeautifulSoup(req.content, 'html.parser')
		scriptText = soup.select('.scrtext pre pre')
		for i in scriptText:
			print(i.text)
