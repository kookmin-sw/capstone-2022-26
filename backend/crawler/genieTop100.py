import requests
from bs4 import BeautifulSoup
import pymysql
from datetime import datetime
from decouple import config
from pymysql.converters import escape_string


def genieCrawling():
    # 1위~50위
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://www.genie.co.kr/chart/top200'
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    info = soup.select("a.btn-basic.btn-info")
    url_list = []

    for i in info:
        url_list.append("https://www.genie.co.kr/detail/songInfo?xgnm="+str(i["onclick"][16:24]))

    trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    list_song = []
    list_artist = []
    list_cover = []
    list_rank = []

    for tr in trs:
        rank = int(tr.select_one('td.number').text[0:2].strip())
        title = tr.select_one('td.info > a.title.ellipsis').text.replace("19금\n", "").strip()
        artist = tr.select_one('td.info > a.artist.ellipsis').text
        cover = "https:" + tr.select_one('td > a img')['src']

        list_rank.append(rank)
        list_song.append(title)
        list_artist.append(artist)
        list_cover.append(cover)

    # 50위~100위
    url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20220326&hh=09&rtm=Y&pg=2'

    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    info = soup.select("a.btn-basic.btn-info")

    for i in info:
        url_list.append("https://www.genie.co.kr/detail/songInfo?xgnm="+str(i["onclick"][16:24]))

    trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')


    for tr in trs:
        rank = int(tr.select_one('td.number').text[0:3].strip())
        title = tr.select_one('td.info > a.title.ellipsis').text.replace("19금\n", "").strip()
        artist = tr.select_one('td.info > a.artist.ellipsis').text
        cover = "https:" + tr.select_one('td > a img')['src']

        list_rank.append(rank)
        list_song.append(title)
        list_artist.append(artist)
        list_cover.append(cover)
    return list_rank, list_song, list_artist, list_cover, url_list

def genieHeart(url_list):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    list_heart = []

    for i in url_list:
        url = i
        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        info = soup.select("em#emLikeCount")

        list_heart.append(int(info[0].get_text().replace(",","")))

    return list_heart

