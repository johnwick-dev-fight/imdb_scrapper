import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.5"
}
data = requests.get(url,headers=headers)
print(data.status_code)

html = data.text

aman= BeautifulSoup(html,'html.parser')
item=aman.find_all('li', class_='ipc-metadata-list-summary-item')
name=[]
year=[]
time=[]
rating=[]
for i in item:
  name.append(i.find('h3', class_='ipc-title__text').text)
  year.append(i.find_all('div',class_='hTMtRz')[0].find_all('span')[0].text)
  time.append(i.find_all('div',class_='hTMtRz')[0].find_all('span')[1].text)
  rating.append(i.find_all('div',class_='hTMtRz')[0].find_all('span')[2].text)

df=pd.DataFrame({
    'Title':name,
    'Year':year,
    'Time':time,
    'Rating':rating
})
df.to_csv('imdb_top_movies.csv', index=False)
