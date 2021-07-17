import requests
from bs4 import BeautifulSoup

area = input()
webpage = requests.get('https://www.google.com/search?q=날씨+' + area)
soup = BeautifulSoup(webpage.text, "html.parser")

title = soup.find_all(attrs={'class': 'tAd8D'})
temp = soup.find(attrs={'class': 'iBp4i'})
others = soup.find_all(attrs={'class': 's3v9rd'})
current_time = soup.find()

print('날씨 정보 \n')
print(title[0].get_text())
print(title[1].get_text())
print(temp.get_text())

