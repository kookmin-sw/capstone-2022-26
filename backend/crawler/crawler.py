import bugsTop100
import genieTop100
import melonTop100
from datetime import datetime
import pymysql
from pymysql.converters import escape_string
from decouple import config


class DB_Utils:

    def queryExecutor(self, db, sql, params, commit):
        conn = pymysql.connect(host=config('DB_HOST'), port=int(config('DB_PORT')), user=config('DB_USER'), password=config('DB_PASSWORD'), db=config('DB_NAME'), charset='utf8')
        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:     # dictionary based cursor
                cursor.execute(sql, params)
                if commit==1:
                    conn.commit()
                else:
                    tuples = cursor.fetchall()
                    return tuples
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()

class DB_Queries:
    # 모든 검색문은 여기에 각각 하나의 메소드로 정의

    def saveCrawlingData(self, site, item):
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
        util = DB_Utils()
        params = ()
        util.queryExecutor(db=config('DB_NAME'), sql=sql, params=params, commit=1)
    
    
    def saveTotalData(self, item):
        # DB에 저장하는 Query문

        sql = """INSERT INTO api_total VALUES(
            NULL,
            '""" + str(item['total_rank']) + """',
            '""" + escape_string(item['song']) + """',
            '""" + escape_string(item['artist']) + """',
            '""" + item['coverImg'] + """',
            '""" + str(item['date']) + """',
            '""" + str(item['time']) + """',
            '""" + str(item['weight']) + """')"""
        util = DB_Utils()
        params = ()
        util.queryExecutor(db=config('DB_NAME'), sql=sql, params=params, commit=1)

    def totalChart(self):
        sql = """(select * from (SELECT * FROM api_bugs order by b_date desc limit 100) b 
        left outer join (select * from api_genie order by g_date desc limit 100) g 
        on b.b_song=g.g_song 
        left outer join (select * from api_melon order by m_date desc limit 100) m 
        on b.b_song=m.m_song order by b_date) 
        union 
        (select * from (SELECT * FROM api_bugs order by b_date desc limit 100) b 
        right outer join (select * from api_genie order by g_date desc limit 100) g 
<<<<<<< HEAD
        on g.g_song=b.b_song 
=======
        on g.g_song=b.b_song  
>>>>>>> 542178391417a2dc0944e8dd2591722cb72b6fbc
        left outer join (select * from api_melon order by m_date desc limit 100) m 
        on g.g_song=m.m_song order by b_date)
         union 
        (select * from (SELECT * FROM api_bugs order by b_date desc limit 100) b 
        right outer join  ((select * from api_genie order by g_date desc limit 100) g 
        right outer join (select * from api_melon order by m_date desc limit 100) m 
        on m.m_song=g.g_song) on m.m_song=b.b_song order by b_date)"""
        util = DB_Utils()
        params = ()
        tuples = util.queryExecutor(db=config('DB_NAME'), sql=sql, params=params, commit=0)
        for rowIDX in range(len(tuples)):
            if tuples[rowIDX]['g_weight'] == None:
                tuples[rowIDX]['g_weight'] = 0
            if tuples[rowIDX]['b_weight'] == None:
                tuples[rowIDX]['b_weight'] = 0
            if tuples[rowIDX]['m_weight'] == None:
                tuples[rowIDX]['m_weight'] = 0
            tuples[rowIDX]['total_weight'] = tuples[rowIDX]['b_weight'] + tuples[rowIDX]['m_weight'] + tuples[rowIDX]['g_weight']

        tuples = sorted(tuples, key=lambda x: (-x['total_weight']))
        for rowIDX in range(100):
            tmp = {}
            tmp['total_rank'] = rowIDX+1
            tmp['date'] = datetime.now()  # 크롤링한 시간이 지니, 멜론, 벅스별로 다르기 때문에 저장된 시간으로 하면 정렬 이상해져서
            tmp['time'] = datetime.now().time()  # 현재 시간 새로 저장. 크롤링이랑 동시에 실행해야 할 듯
            tmp['weight'] = tuples[rowIDX]['total_weight']
            if tuples[rowIDX]['m_rank'] == None:
                if tuples[rowIDX]['g_rank'] == None:
                    tmp['song'] = tuples[rowIDX]['b_song']
                    tmp['artist'] = tuples[rowIDX]['b_artist']
                    tmp['coverImg'] = tuples[rowIDX]['b_coverImg']
                else:
                    tmp['song'] = tuples[rowIDX]['g_song']
                    tmp['artist'] = tuples[rowIDX]['g_artist']
                    tmp['coverImg'] = tuples[rowIDX]['g_coverImg']
            else:
                tmp['song'] = tuples[rowIDX]['m_song']
                tmp['artist'] = tuples[rowIDX]['m_artist']
                tmp['coverImg'] = tuples[rowIDX]['m_coverImg']

            self.saveTotalData(tmp)


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


query = DB_Queries()


for i in range (100):
    bugsSong_dict['rank'] = bugsRank[i]
    bugsSong_dict['song'] = bugsSong[i]
    bugsSong_dict['artist'] = bugsArtist[i]
    bugsSong_dict['heart'] = bugsHeart[i]
    bugsSong_dict['coverImg'] = bugsCover[i]
    bugsSong_dict['date'] = datetime.now()
    bugsSong_dict['time'] = datetime.now().time()
    bugsSong_dict['weight'] = (101-bugsRank[i])*bugsWeight
    query.saveCrawlingData("bugs", bugsSong_dict)

    genieSong_dict['rank'] = genieRank[i]
    genieSong_dict['song'] = genieSong[i]
    genieSong_dict['artist'] = genieArtist[i]
    genieSong_dict['heart'] = genieHeart[i]
    genieSong_dict['coverImg'] = genieCover[i]
    genieSong_dict['date'] = datetime.now()
    genieSong_dict['time'] = datetime.now().time()
    genieSong_dict['weight'] = (101-genieRank[i])*genieWeight
    query.saveCrawlingData("genie", genieSong_dict)

    melonSong_dict['rank'] = melonRank[i]
    melonSong_dict['song'] = melonSong[i]
    melonSong_dict['artist'] = melonArtist[i]
    melonSong_dict['heart'] = melonHeart[i]
    melonSong_dict['coverImg'] = melonCover[i]
    melonSong_dict['date'] = datetime.now()
    melonSong_dict['time'] = datetime.now().time()
    melonSong_dict['weight'] = (101 - melonRank[i]) * melonWeight
    query.saveCrawlingData("melon", melonSong_dict)

query.totalChart()
