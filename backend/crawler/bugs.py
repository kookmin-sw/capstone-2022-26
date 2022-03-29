import requests
from bs4 import BeautifulSoup
import multiprocessing
from datetime import datetime
from typing import Dict

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from api.models import ChartData
ChartData.objects.all().delete()
class Bugs:
    URL = "https://music.bugs.co.kr/chart"
    data: Dict = None

    def __init__(self):
        url = self.URL
        response = requests.get(url)
        tracks_list = []
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            tracks = soup.select("#CHARTrealtime > table > tbody > tr")
            trackInfo_list = []
            for track in tracks:
                trackInfoUrl = track.select_one("td > a.trackInfo").attrs["href"]
                trackInfo_list.append(trackInfoUrl)

            like_list = self.thread_crawl(trackInfo_list)

            for i, track in enumerate(tracks):
                rank = track.select_one("td > div.ranking > strong").get_text()
                title = track.select_one("th > p > a").get_text()
                artist = track.select_one("td > p.artist > a").get_text()
                trackImg = track.select_one("td > a > img").attrs["src"]
                tracks_list.append({
                    "rank": rank,
                    "title": title,
                    "artist": artist,
                    "img": trackImg,
                    "like": like_list[i]
                })
                ChartData (
                    # site =  "Bugs",
                    # dateTime =  datetime.now().strftime("%y%m%d%H"),
                    rank_t = rank,
                    title_t = title,
                    artist_t =  artist,
                    img = trackImg,
                    like = like_list[i]
                ).save()
            # Bugs.data = {
            #     "site": "Bugs",
            #     "dateTime": datetime.strftime("%y%m%d%h"),
            #     "tracks": tracks_list
            # }
            # ChartData (
            #     # site =  "Bugs",
            #     # dateTime =  datetime.now().strftime("%y%m%d%H"),
            #     rank_t = rank,
            #     title_t = title,
            #     artist_t =  artist,
            #     img = trackImg,
            #     like = like_list[i]
            # ).save()
        else:
            print("error")

    def thread_crawl(self, urls: list):
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        results = [pool.apply_async(self.like_crawl, (url,)) for url in urls]
        pool.close()
        pool.join()
        like_list = [res.get() for res in results]
        return like_list

    def like_crawl(self, url: str):
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        return soup.select_one(
            "#container > section.sectionPadding.summaryInfo.summaryTrack > div > div.etcInfo > span > a > span > em").get_text()


if __name__ == '__main__':
    b = Bugs()
