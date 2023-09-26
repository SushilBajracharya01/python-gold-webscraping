import requests
from bs4 import BeautifulSoup
import json

URL='https://gahanaonline.com/gold-rate-history/'
page = requests.get(URL);

soup = BeautifulSoup(page.content, 'html.parser');

table = soup.find('table')

elements = table.find_all("tr")
 
results = []
for element in elements:
    children = element.findChildren("td")
    results.append({'date_ad': children[0].text.strip(),'date_bs': children[1].text.strip(),'amount': children[2].text.strip().replace("/-","")})


with open('goldlog.json', 'w', encoding='latin-1') as f:
    json.dump(results, f, indent=8, ensure_ascii=False)
print("Created Json File")