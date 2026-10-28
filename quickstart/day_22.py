# Day 22: web scraping   (pip install requests beautifulsoup4)
import json

import requests
from bs4 import BeautifulSoup

url = 'http://www.scrapethissite.com/pages/forms/'       # a site built for scraping practice
headers = {'User-Agent': 'Mozilla/5.0'}                   # some sites (Wikipedia) block requests without one
soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')

print(soup.title.get_text(strip=True))
table = soup.find('table')                                # first <table>; find_all() = every one

rows = []
for tr in table.find_all('tr'):                           # every row
    rows.append([cell.get_text(strip=True) for cell in tr.find_all(['th', 'td'])])

header, *body = rows
records = [dict(zip(header, row)) for row in body]       # row -> {column: value}
print(len(records), records[0])

with open('scraped.json', 'w', encoding='utf-8') as f:   # save as JSON
    json.dump(records, f, indent=2)
