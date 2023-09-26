import requests
from bs4 import BeautifulSoup

URL='https://gahanaonline.com/gold-rate-history/'
page = requests.get(URL);

soup = BeautifulSoup(page.content, 'html.parser');

table = soup.find('table')

elements = table.find_all("tr")

results = []
for element in elements:
    children = element.findChildren()
    for child in children:
        data = {}
        print(child)
        # data.date_ad = child[0].text
        # data.date_bs = child[1].text
        # data.amount = child[2].text
        # results.insert(data)

print(results)    
