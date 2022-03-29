import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os

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
        rank = song_tag.select_one('.rank').text

        #album 커버 저장
        createFolder('./melon_cover')
        urlretrieve(coverImg, './melon_cover/'+song+".png")

        song = {
            'songNo': songNo,
            'rank': rank,
            'song': song,
            'artist': artist,
            'album': album,
            'coverImg': coverImg,
        }

        song_list.append(song)

    song_df = pd.DataFrame(song_list, columns=['rank', 'songNo', 'album', 'song', 'artist', 'coverImg']).set_index('songNo')


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


melon100 = melonTop100()


for i in range (100):
    print(melon100.iloc[i]['song'], melon100.iloc[i]['artist'], melon100.iloc[i]['heart'])


print(sum(melon100['heart']))