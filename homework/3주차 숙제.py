import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr.list')

rank = 1
for song in songs:
    a_tag = song.select_one('td.info > a.title')
    if a_tag is not None:
        title = a_tag.text
        artist = song.select_one('td.info > a.artist').text
        print(rank,title.strip(),artist)
        rank += 1