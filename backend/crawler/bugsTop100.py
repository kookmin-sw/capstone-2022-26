import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os



def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


def bugsCrawling():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://music.bugs.co.kr/chart'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    info = soup.select("a.trackInfo")
    songs = soup.select('p.title')
    singers = soup.select('p.artist')
    covers = soup.select('#CHARTrealtime tbody tr a img')

    list_song = [song.text.replace("[19금]\n", "").strip() for song in songs]
    list_artist = [singer.text.strip() for singer in singers]
    list_cover = [cover['src'] for cover in covers]

    url_list = []

    for i in info:
        url_list.append(i['href'])

    return list_song, list_artist, list_cover, url_list


def bugsHeart(list_song, list_cover, url_list):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    #앨범 커버 저장
    createFolder('./bugs_cover')

    for i in range(100):
        urlretrieve(list_cover[i], './bugs_cover/' +  list_song[i]+ ".png")

    list_heart = []

    for i in url_list:
        url = i
        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        info = soup.select("em")

        list_heart.append(int(info[0].get_text().replace(",","")))

    return list_heart

song, artist, cover, url = bugsCrawling()
heart = bugsHeart(song, cover, url)

print(song)
print(artist)
print(heart)
print(sum(heart))