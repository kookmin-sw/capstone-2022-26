import bugsTop100
import genieTop100
import melonTop100
from datetime import datetime
import pymysql
from pymysql.converters import escape_string
from decouple import config


bugsRank, bugsSong, bugsArtist, bugsCover, bugsUrl = bugsTop100.bugsCrawling()
bugsHeart = bugsTop100.bugsHeart(bugsUrl)
bugsSong_dict = dict()

genieRank, genieSong, genieArtist, genieCover, genieUrl = genieTop100.genieCrawling()
genieHeart = genieTop100.genieHeart(genieUrl)
genieSong_dict = dict()

melonRank, melonSong, melonArtist, melonCover, melonHeart = melonTop100.melonTop100()
melonSong_dict = dict()


bugsTotalHeart = sum(bugsHeart)
genieTotalHeart = sum(genieHeart)
melonTotalHeart = sum(melonHeart)
totalHeart = bugsTotalHeart+genieTotalHeart+melonTotalHeart

bugsWeight = bugsTotalHeart/totalHeart
genieWeight = genieTotalHeart/totalHeart
melonWeight = melonTotalHeart/totalHeart

db = pymysql.connect(host=config('DB_HOST'), port=int(config('DB_PORT')), user=config('DB_USER'), password=config('DB_PASSWORD'), db=config('DB_NAME'), charset='utf8')
cursor = db.cursor()

def saveDB(site, item):
    # DB에 저장하는 Query문
    api = "api_" + site
    sql = """INSERT INTO """ + api + """ VALUES(
        NULL,
        '""" + str(item['rank']) + """',
        '""" + escape_string(item['song']) + """',
        '""" + escape_string(item['artist']) + """',
        '""" + str(item['heart']) + """',
        '""" + item['coverImg'] + """',
        '""" + str(item['date']) + """',
        '""" + str(item['time']) + """',
        '""" + str(item['weight']) + """')"""

    cursor.execute(sql)



for i in range (100):
    bugsSong_dict['rank'] = bugsRank[i]
    bugsSong_dict['song'] = bugsSong[i]
    bugsSong_dict['artist'] = bugsArtist[i]
    bugsSong_dict['heart'] = bugsHeart[i]
    bugsSong_dict['coverImg'] = bugsCover[i]
    bugsSong_dict['date'] = datetime.now()
    bugsSong_dict['time'] = datetime.now().time()
    bugsSong_dict['weight'] = (101-bugsRank[i])*bugsWeight
    saveDB("bugs", bugsSong_dict)

    genieSong_dict['rank'] = genieRank[i]
    genieSong_dict['song'] = genieSong[i]
    genieSong_dict['artist'] = genieArtist[i]
    genieSong_dict['heart'] = genieHeart[i]
    genieSong_dict['coverImg'] = genieCover[i]
    genieSong_dict['date'] = datetime.now()
    genieSong_dict['time'] = datetime.now().time()
    genieSong_dict['weight'] = (101-genieRank[i])*genieWeight
    saveDB("genie", genieSong_dict)

    melonSong_dict['rank'] = melonRank[i]
    melonSong_dict['song'] = melonSong[i]
    melonSong_dict['artist'] = melonArtist[i]
    melonSong_dict['heart'] = melonHeart[i]
    melonSong_dict['coverImg'] = melonCover[i]
    melonSong_dict['date'] = datetime.now()
    melonSong_dict['time'] = datetime.now().time()
    melonSong_dict['weight'] = (101 - melonRank[i]) * melonWeight
    saveDB("melon", melonSong_dict)

db.commit()
db.close()