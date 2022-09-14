import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.dailysmarty.com/topics/python')
# r = requests.get('https://www.bodybuilding.com/fun/articles')

# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)
links = soup.find_all('a')
# print(links)

for link in links:
    print(link['href'])
