from numpy import save
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
import pymysql
from datetime import datetime
from decouple import config
from pymysql.converters import escape_string

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


pd.set_option('display.max_row', 1000)
pd.set_option('display.max_columns', 1000)


def melonTop100():

    url = 'http://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }
    html = requests.get(url, headers=headers).text


    soup = BeautifulSoup(html, 'html.parser')


    song_list = []

    for song_tag in soup.select('#tb_list tbody tr'):
        songNo = song_tag['data-song-no']
        coverImg = song_tag.select_one('img')['src']
        song = song_tag.select_one('a[href*=playSong]').text
        artist = song_tag.select_one('a[href*=goArtistDetail]').text
        album = song_tag.select_one('a[href*=goAlbumDetail]')['title']
        rank = int(song_tag.select_one('.rank').text)
        crawlingTime = datetime.now()
        # crawlingTime = timezone.make_aware(crawlingTime)
        #album 커버 저장
        # createFolder('./melon_cover')
        # urlretrieve(coverImg, './melon_cover/'+song+".png")

        now = datetime.now()

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

    song_df = pd.DataFrame(song_list, columns=['rank', 'songNo', 'album', 'song', 'artist', 'coverImg', 'crawlingTime']).set_index('songNo')


    song_id_list = song_df.index

    # 노래별 "좋아요" 정보 획득
    url = 'http://www.melon.com/commonlike/getSongLike.json'
    params = {
        'contsIds': song_id_list,
    }
    result = requests.get(url, headers=headers, params=params).json()
    like_dict = { str(song['CONTSID']):song['SUMMCNT'] for song in result['contsLike'] }

    # 좋아요 정보 추가
    song_df['heart'] = pd.Series(like_dict)

    return song_df

def saveDB(item):
    sql = """INSERT INTO api_melon VALUES(
        NULL,
        '""" + str(item['rank']) + """',
        '""" + escape_string(item['song']) + """',
        '""" + escape_string(item['artist']) + """',
        '""" + str(item['heart']) + """',
        '""" + item['coverImg'] + """',
        '""" + str(item['crawlingTime']) + """')"""
    cursor.execute(sql)

melon100 = melonTop100()
song_dict = dict()

db = pymysql.connect(host=config('DB_HOST'), port=int(config('DB_PORT')), user=config('DB_USER'), password=config('DB_PASSWORD'), db=config('DB_NAME'), charset='utf8')
cursor = db.cursor()

for i in range (100):
    song_dict['rank'] = melon100.iloc[i]['rank']
    song_dict['song'] = melon100.iloc[i]['song']
    song_dict['artist'] = melon100.iloc[i]['artist']
    song_dict['heart'] = melon100.iloc[i]['heart']
    song_dict['coverImg'] = melon100.iloc[i]['coverImg']
    song_dict['crawlingTime'] = melon100.iloc[i]['crawlingTime']
    saveDB(song_dict)

db.commit()
db.close()