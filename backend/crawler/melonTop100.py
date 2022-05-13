import requests
import pandas as pd
from bs4 import BeautifulSoup
import pymysql
from datetime import datetime
from decouple import config
from pymysql.converters import escape_string


pd.set_option('display.max_row', 1000)
pd.set_option('display.max_columns', 1000)


def melonTop100():

    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }
    html = requests.get(url, headers=headers).text


    soup = BeautifulSoup(html, 'html.parser')


    song_list = []
    list_song = []
    list_artist = []
    list_cover = []
    list_rank = []
    list_songNo = []
    list_heart = []

    for song_tag in soup.select('#tb_list tbody tr'):
        songNo = song_tag['data-song-no']
        coverImg = song_tag.select_one('img')['src']
        song = song_tag.select_one('a[href*=playSong]').text
        artist = song_tag.select_one('a[href*=goArtistDetail]').text
        album = song_tag.select_one('a[href*=goAlbumDetail]')['title']
        rank = int(song_tag.select_one('.rank').text)
        crawlingTime = datetime.now()


        list_rank.append(rank)
        list_song.append(song)
        list_artist.append(artist)
        list_cover.append(coverImg)
        list_songNo.append(songNo)

        song = {
            'songNo': songNo,
            'rank': rank,
            'song': song,
            'artist': artist,
            'album': album,
            'coverImg': coverImg,
            'crawlingTime': crawlingTime
        }

        song_list.append(song)

    # song_df = pd.DataFrame(song_list, columns=['rank', 'songNo', 'album', 'song', 'artist', 'coverImg', 'crawlingTime']).set_index('songNo')

    # song_id_list = song_df.index

    # 노래별 "좋아요" 정보 획득
    url = 'http://www.melon.com/commonlike/getSongLike.json'
    params = {
        'contsIds': list_songNo,
    }
    result = requests.get(url, headers=headers, params=params).json()
    like_dict = { str(song['CONTSID']):song['SUMMCNT'] for song in result['contsLike'] }
    # 좋아요 정보 추가
    # song_df['heart'] = pd.Series(like_dict)

    for key, value in like_dict.items():
        list_heart.append(value)
        
    return list_rank, list_song, list_artist, list_cover, list_heart

# Function for saving to DB
def saveDB(item):
    # DB에 저장하는 Query문
    sql = """INSERT INTO api_melon VALUES(
        NULL,
        '""" + str(item['rank']) + """',
        '""" + escape_string(item['song']) + """',
        '""" + escape_string(item['artist']) + """',
        '""" + str(item['heart']) + """',
        '""" + item['coverImg'] + """',
        '""" + str(item['crawlingTime']) + """')"""
    cursor.execute(sql)

rank, song, artist, cover, heart = melonTop100()
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