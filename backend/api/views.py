from django import views
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Melon, Genie, Bugs
from .serializer import MelonSerializer, GenieSerializer, BugsSerializer
from rest_framework.views import APIView
from datetime import datetime, timedelta
import pymysql
from decouple import config
from datetime import datetime

# 통합 차트 및 3개 차트 View
class ChartView(viewsets.ViewSet):
    melon_queryset = Melon.objects
    bugs_queryset = Bugs.objects
    genie_queryset = Genie.objects

    def list(self, request):
        # 가중치를 이용한 통합 순위 계산(미구현) 
        query = DB_Queries()
        chartData = query.totalChart()
        return Response(chartData)
    

    # 최신 Melon top 100 순위(순위가 100부터 1 순으로 리턴)
    @action(detail=False, methods=['get'])
    def melon(self, request):
        # query = DB_Queries()
        # melon = query.currentTimeChart("api_melon")
        # return Response(melon)
        # 뒤에서 100개의 곡을 가져온다, slicing 후 재정렬이 어려워 역순으로 리턴
        queryset = self.melon_queryset.order_by('-id')[:100]
        # queryset = queryset.order_by('id')
        serialized_melon = MelonSerializer(queryset, many=True)
        return Response(data=serialized_melon.data)

    # 최신 Bugs top 100 순위 
    @action(detail=False, methods=['get'])
    def bugs(self, request):
        # query = DB_Queries()
        # bugs = query.currentTimeChart("api_bugs")
        # return Response(bugs)
        # 뒤에서 100개의 곡을 가져온다, slicing 후 재정렬이 어려워 역순으로 리턴
        queryset = self.bugs_queryset.order_by('-id')[:100]
        serialized_genie = BugsSerializer(queryset, many=True)
        return Response(data=serialized_genie.data)

    # 최신 Genie top 100 순위 
    @action(detail=False, methods=['get'])
    def genie(self, request):
        # query = DB_Queries()
        # genie = query.currentTimeChart("api_genie")
        # return Response(genie)
        # 뒤에서 100개의 곡을 가져온다, slicing 후 재정렬이 어려워 역순으로 리턴
        queryset = self.genie_queryset.order_by('-id')[:100]
        serialized_genie = GenieSerializer(queryset, many=True)
        return Response(data=serialized_genie.data)


# 각 곡에 대한 세부 정보 View
class TrackView(APIView):
    def get(self, request, pk):
        param = request.GET.get('artist')
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H")
        
        melon_queryset = Melon.objects.filter(m_song=pk, m_artist=param, m_time=current_time)
        bugs_queryset = Bugs.objects.filter(b_song=pk, b_artist=param, b_time=current_time)
        genie_queryset = Genie.objects.filter(g_song=pk, g_artist=param, g_time=current_time)

        current_melon_queryset = Melon.objects.filter(m_song=pk, m_artist=param, m_date=current_date, m_time=current_time)
        current_bugs_queryset = Bugs.objects.filter(b_song=pk, b_artist=param, b_date=current_date, b_time=current_time)
        current_genie_queryset = Genie.objects.filter(g_song=pk, g_artist=param, g_date=current_date, g_time=current_time)

        # 크롤링 시간이 걸려 정각에 바로 갱신되지 않는 경우 갱신 전 데이터를 불러옴
        if not current_melon_queryset.exists() and not current_bugs_queryset.exists() and not current_genie_queryset.exists():
            current_date = (datetime.now() - timedelta(hours=1)).strftime("%Y-%m-%d")
            current_time = (datetime.now() - timedelta(hours=1)).strftime("%H")
            melon_queryset = Melon.objects.filter(m_song=pk, m_artist=param, m_time=current_time)
            bugs_queryset = Bugs.objects.filter(b_song=pk, b_artist=param, b_time=current_time)
            genie_queryset = Genie.objects.filter(g_song=pk, g_artist=param, g_time=current_time)

        if not melon_queryset.exists() and not bugs_queryset.exists() and not genie_queryset.exists():
            return HttpResponseBadRequest()

        serialized_melon = MelonSerializer(melon_queryset, many=True)
        serialized_bugs = BugsSerializer(bugs_queryset, many=True)
        serialized_genie = GenieSerializer(genie_queryset, many=True)

        m_dayBefore = m_yesterday = m_today = b_dayBefore = b_yesterday = b_today = g_dayBefore = g_yesterday = g_today = None

        if serialized_melon.data:
            coverImg = serialized_melon.data[0]['m_coverImg']
        elif serialized_bugs.data:
            coverImg = serialized_bugs.data[0]['b_coverImg']
        elif serialized_genie.data:
            coverImg = serialized_genie.data[0]['g_coverImg']


        for melon_data in serialized_melon.data:
            date = melon_data['m_date']

            if date == (datetime.now() - timedelta(2)).strftime("%Y-%m-%d"):
                m_dayBefore = melon_data['m_rank']

            elif date == (datetime.now() - timedelta(1)).strftime("%Y-%m-%d"):
                m_yesterday = melon_data['m_rank']

            elif date == datetime.now().strftime("%Y-%m-%d"):
                m_today = melon_data['m_rank']

        for bugs_data in serialized_bugs.data:
            date = bugs_data['b_date']
            
            if date == (datetime.now() - timedelta(2)).strftime("%Y-%m-%d"):
                b_dayBefore = bugs_data['b_rank']

            elif date == (datetime.now() - timedelta(1)).strftime("%Y-%m-%d"):
                b_yesterday = bugs_data['b_rank']

            elif date == datetime.now().strftime("%Y-%m-%d"):
                b_today = bugs_data['b_rank']

        for genie_data in serialized_genie.data:
            date = genie_data['g_date']

            if date == (datetime.now() - timedelta(2)).strftime("%Y-%m-%d"):
                g_dayBefore = genie_data['g_rank']

            elif date == (datetime.now() - timedelta(1)).strftime("%Y-%m-%d"):
                g_yesterday = genie_data['g_rank']

            elif date == datetime.now().strftime("%Y-%m-%d"):
                g_today = genie_data['g_rank']


        trackData = {'track':pk, 'artist':param, 'coverImg':coverImg, 'date': current_date, 'time': int(current_time), 'melon': {'dayBefore': m_dayBefore, 'yesterday': m_yesterday, 'today': m_today},
            'bugs': {'dayBefore': b_dayBefore, 'yesterday': b_yesterday, 'today': b_today},
            'genie': {'dayBefore': g_dayBefore, 'yesterday': g_yesterday, 'today': g_today}}

        return Response(data=trackData)

class DB_Utils:

    def queryExecutor(self, db, sql, params):
        conn = pymysql.connect(host=config('DB_HOST'), port=int(config('DB_PORT')), user=config('DB_USER'), password=config('DB_PASSWORD'), db=config('DB_NAME'), charset='utf8')

        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:     # dictionary based cursor
                cursor.execute(sql, params)
                tuples = cursor.fetchall()
                return tuples
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()


class DB_Queries:
    # 모든 검색문은 여기에 각각 하나의 메소드로 정의

    def currentTimeChart(self, site):
        sql = "SELECT * FROM "
        sql2 = site + " where date='" + str(datetime.now().date()) + "' and time=" + str(datetime.now().hour)
        sql += sql2
        util = DB_Utils()
        params = ()
        tuples = util.queryExecutor(db=config('DB_NAME'), sql=sql, params=params)
        return tuples
    def totalChart(self):
        sql = """(select * from (SELECT * FROM api_bugs order by b_date desc limit 100) b 
        left outer join (select * from api_genie order by g_date desc limit 100) g 
        on b.b_song=g.g_song and b.b_artist=g.g_artist 
        left outer join (select * from api_melon order by m_date desc limit 100) m 
        on b.b_song=m.m_song and b.b_artist=m.m_artist order by b_date) 
        union 
        (select * from (SELECT * FROM api_bugs order by b_date desc limit 100) b 
        right outer join (select * from api_genie order by g_date desc limit 100) g 
        on g.g_song=b.b_song and g.g_artist=b.b_artist 
        left outer join (select * from api_melon order by m_date desc limit 100) m 
        on g.g_song=m.m_song and g.g_artist=m.m_artist order by b_date)
         union 
        (select * from (SELECT * FROM api_bugs order by b_date desc limit 100) b 
        right outer join  ((select * from api_genie order by g_date desc limit 100) g 
        right outer join (select * from api_melon order by m_date desc limit 100) m 
        on m.m_song=g.g_song and g.g_artist=m.m_artist) on m.m_song=b.b_song and m.m_artist=b.b_artist order by b_date)"""
        util = DB_Utils()
        params = ()
        tuples = util.queryExecutor(db=config('DB_NAME'), sql=sql, params=params)
        for rowIDX in range(len(tuples)):
            if tuples[rowIDX]['g_weight'] == None:
                tuples[rowIDX]['g_weight'] = 0
            if tuples[rowIDX]['b_weight'] == None:
                tuples[rowIDX]['b_weight'] = 0
            if tuples[rowIDX]['m_weight'] == None:
                tuples[rowIDX]['m_weight'] = 0
            tuples[rowIDX]['g_weight'] += tuples[rowIDX]['b_weight'] + tuples[rowIDX]['m_weight']
        tuples = sorted(tuples, key=lambda x: (-x['g_weight']))
        return tuples