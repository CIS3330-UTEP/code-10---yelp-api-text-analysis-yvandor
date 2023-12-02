from bs4 import BeautifulSoup
import requests

web_url= 'https://www.utep.edu/business/people/faculty-profiles.html'
page_to_scrape = requests.get(web_url)

soup = BeautifulSoup(page_to_scrape.text,'html.parser')
info_tags = soup.findAll ('div', attrs={'class': 'infoCol'})

for tag in info_tags:
    professor = {}
    #print (tag)
    professor['name'] =tag.find('h3', attrs={'class':'name'}).text
    professor['title'] = tag.find ('span', attrs={'class':'Title'}).text

if tag.find('span', attrs={'class':'email'}) is not None:
    professor['email'] = tag.find('span', attrs= {'class':'email'}).text
else:
    professor['email'] ="N/A"

if tag.find('span', attrs={'class':'phone'})is not None:
    professor['phone'] = tag.find('span', attrs={'class':'phone'}).text
else:
    professor['phone'] = "N/A"

print(professor)