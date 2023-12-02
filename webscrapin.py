from bs4 import BeautifulSoup
import requests

web_url= 'https://www.utep.edu/business/people/faculty-profiles.html'
page_to_scrape = requests.get(web_url)

soup = BeautifulSoup(page_to_scrape.text,'html.parser')
emails = soup.findALL('span',attrs={'class':'email'})
for tag in emails:
    print(tag.text)