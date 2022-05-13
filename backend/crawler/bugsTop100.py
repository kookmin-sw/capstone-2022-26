import requests
from bs4 import BeautifulSoup
import pymysql
from datetime import datetime
from decouple import config
from pymysql.converters import escape_string

def bugsCrawling():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://music.bugs.co.kr/chart'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    info = soup.select("a.trackInfo")
    ranks = soup.select("td > div.ranking > strong")
    songs = soup.select('p.title')
    singers = soup.select('p.artist')
    covers = soup.select('#CHARTrealtime tbody tr a img')

    list_rank = [int(rank.text) for rank in ranks]
    list_song = [song.text.replace("[19금]\n", "").strip() for song in songs]
    list_artist = [singer.text.strip() for singer in singers]
    list_cover = [cover['src'] for cover in covers]

    url_list = []
    for i in info:
        url_list.append(i['href'])

    return list_rank, list_song, list_artist, list_cover, url_list


def bugsHeart(list_song, list_cover, url_list):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    list_heart = []

    for i in url_list:
        url = i
        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        info = soup.select("em")

        list_heart.append(int(info[0].get_text().replace(",","")))

    return list_heart

# Function for saving to DB
def saveDB(item):
    # DB에 저장하는 Query문
    sql = """INSERT INTO api_bugs VALUES(
        NULL,
        '""" + str(item['rank']) + """',
        '""" + escape_string(item['song']) + """',
        '""" + escape_string(item['artist']) + """',
        '""" + str(item['heart']) + """',
        '""" + item['coverImg'] + """',
        '""" + str(item['crawlingTime']) + """')"""
    cursor.execute(sql)

rank, song, artist, cover, url = bugsCrawling()
heart = bugsHeart(song, cover, url)
song_dict = dict()

# AWS RDS(MySQL) DB 연결
db = pymysql.connect(host=config('DB_HOST'), port=int(config('DB_PORT')), user=config('DB_USER'), password=config('DB_PASSWORD'), db=config('DB_NAME'), charset='utf8')
cursor = db.cursor()

# 각 곡에 대한 data 저장
for i in range (100):
    song_dict['rank'] = rank[i]
    song_dict['song'] = song[i]
    song_dict['artist'] = artist[i]
    song_dict['heart'] = heart[i]
    song_dict['coverImg'] = cover[i]
    song_dict['crawlingTime'] = datetime.now()
    saveDB(song_dict)

db.commit()
db.close()
