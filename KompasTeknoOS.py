import requests
from bs4 import BeautifulSoup
import csv

location = "https://tekno.kompas.com/apps-os"
req = requests.get(location)

soup = BeautifulSoup(req.text, 'html.parser')
news  = soup.select('div.article__list.clearfix')
data = []
for row in news:
    title = row.select('h3.article__title.article__title--medium')[0].text.encode('utf-8')
    link  = row.select('h3.article__title.article__title--medium > a')[0]['href']
    lokasi_isi = requests.get(link)
    soup = BeautifulSoup(lokasi_isi.text, 'html.parser')
    isi = soup.select('div.read__content')[0].text.encode('utf-8')
    data.append([title, isi])

    print data
with open('data-kompas.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)