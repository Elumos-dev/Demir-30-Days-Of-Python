# Day 20: pip and reading data from the web
# Terminal:  pip install requests      pip list      pip show requests
#            pip freeze > requirements.txt          pip uninstall requests
import statistics

import requests

r = requests.get('https://www.gutenberg.org/files/1112/1112.txt')   # Ex 1
print(r.status_code, len(r.text.split()))     # 200 = OK, .text = page as a string

r = requests.get('https://api.thecatapi.com/v1/breeds')             # Ex 2
breeds = r.json()                             # JSON -> list of dicts
print(len(breeds), breeds[0]['name'], breeds[0]['weight'])

ws = [3, 5, 4, 6, 4]                          # Ex 2.1-2.2
print(min(ws), max(ws), statistics.mean(ws), statistics.median(ws), round(statistics.stdev(ws), 2))

# Ex 3: restcountries.eu is dead. The live API needs a fields list (max 10):
r = requests.get('https://restcountries.com/v3.1/all?fields=name,area,languages')
print(r.json()[0]['name']['common'])
