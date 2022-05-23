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
        totalChartData = query.totalChart()
        return Response(totalChartData)
    

    # 최신 Melon top 100 순위(순위가 100부터 1 순으로 리턴)
    @action(detail=False, methods=['get'])
    def melon(self, request):
        query = DB_Queries()
        melon = query.currentTimeChart("api_melon")
        return Response(melon)

    # 최신 Bugs top 100 순위 
    @action(detail=False, methods=['get'])
    def bugs(self, request):
        query = DB_Queries()
        bugs = query.currentTimeChart("api_bugs")
        return Response(bugs)

    # 최신 Genie top 100 순위 
    @action(detail=False, methods=['get'])
    def genie(self, request):
        query = DB_Queries()
        genie = query.currentTimeChart("api_genie")
        return Response(genie)

    @action(detail=False, methods=['get'])
    def dashboard(self, request):
        query = DB_Queries()
        dashboard = query.dashboard()
        return Response(dashboard)



# 각 곡에 대한 세부 정보 View
class TrackView(APIView):
    def get(self, request, pk):
        param = request.GET.get('artist')
        current_date = datetime.now()
        current_time = datetime.now().strftime("%H")
        
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
            date = melon_data['m_date'].split('T')[0]

            if date == (datetime.now() - timedelta(2)).strftime("%Y-%m-%d"):
                m_dayBefore = melon_data['m_rank']

            elif date == (datetime.now() - timedelta(1)).strftime("%Y-%m-%d"):
                m_yesterday = melon_data['m_rank']

            elif date == datetime.now().strftime("%Y-%m-%d"):
                m_today = melon_data['m_rank']

        for bugs_data in serialized_bugs.data:
            date = bugs_data['b_date'].split('T')[0]
            
            if date == (datetime.now() - timedelta(2)).strftime("%Y-%m-%d"):
                b_dayBefore = bugs_data['b_rank']

            elif date == (datetime.now() - timedelta(1)).strftime("%Y-%m-%d"):
                b_yesterday = bugs_data['b_rank']

            elif date == datetime.now().strftime("%Y-%m-%d"):
                b_today = bugs_data['b_rank']

        for genie_data in serialized_genie.data:
            date = genie_data['g_date'].split('T')[0]

            if date == (datetime.now() - timedelta(2)).strftime("%Y-%m-%d"):
                g_dayBefore = genie_data['g_rank']

            elif date == (datetime.now() - timedelta(1)).strftime("%Y-%m-%d"):
                g_yesterday = genie_data['g_rank']

            elif date == datetime.now().strftime("%Y-%m-%d"):
                g_today = genie_data['g_rank']


        trackData = {'track':pk, 'artist':param, 'coverImg':coverImg, 'date': current_date.strftime("%Y-%m-%d"), 'time': int(current_time), 'melon': {'dayBefore': m_dayBefore, 'yesterday': m_yesterday, 'today': m_today},
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
    def totalChart(self):
        sql = "SELECT * FROM api_total order by date desc limit 100"
        util = DB_Utils()
        params = ()
        tuples = util.queryExecutor(db=config('DB_NAME'), sql=sql, params=params)
        tuples = sorted(tuples, key=lambda x: (-x['weight']))

        for rowIDX in range(len(tuples)):
            try:
                sql2 = "SELECT link FROM api_youtube where song=%s"
                params = (tuples[rowIDX]['song'])
                util = DB_Utils()
                youtube = util.queryExecutor(db=config('DB_NAME'), sql=sql2, params=params)
                tuples[rowIDX]['link'] = youtube[0]['link']
            except:
                continue
        return tuples

    def currentTimeChart(self, site):
        sql = "SELECT * FROM "
        sql2 = site + " order by id desc limit 100"
        sql += sql2
        util = DB_Utils()
        params = ()
        tuples = util.queryExecutor(db=config('DB_NAME'), sql=sql, params=params)
        chartData = []
        for rowIDX in range(len(tuples)):
            tmp = {}
            if site == "api_bugs":
                tmp['rank'] = tuples[rowIDX]['b_rank']
                tmp['song'] = tuples[rowIDX]['b_song']
                tmp['artist'] = tuples[rowIDX]['b_artist']
                tmp['like'] = tuples[rowIDX]['b_like']
                tmp['coverImg'] = tuples[rowIDX]['b_coverImg']
                tmp['date'] = tuples[rowIDX]['b_date']
                tmp['time'] = tuples[rowIDX]['b_time']
                tmp['weight'] = tuples[rowIDX]['b_weight']
            if site == "api_genie":
                tmp['rank'] = tuples[rowIDX]['g_rank']
                tmp['song'] = tuples[rowIDX]['g_song']
                tmp['artist'] = tuples[rowIDX]['g_artist']
                tmp['like'] = tuples[rowIDX]['g_like']
                tmp['coverImg'] = tuples[rowIDX]['g_coverImg']
                tmp['date'] = tuples[rowIDX]['g_date']
                tmp['time'] = tuples[rowIDX]['g_time']
                tmp['weight'] = tuples[rowIDX]['g_weight']
            if site == "api_melon":
                tmp['rank'] = tuples[rowIDX]['m_rank']
                tmp['song'] = tuples[rowIDX]['m_song']
                tmp['artist'] = tuples[rowIDX]['m_artist']
                tmp['like'] = tuples[rowIDX]['m_like']
                tmp['coverImg'] = tuples[rowIDX]['m_coverImg']
                tmp['date'] = tuples[rowIDX]['m_date']
                tmp['time'] = tuples[rowIDX]['m_time']
                tmp['weight'] = tuples[rowIDX]['m_weight']
            chartData.append(tmp)
        chartData = sorted(chartData, key=lambda x: (-x['weight']))
        return chartData

    def dashboard(self):
        tuples = self.totalChart()
        dashboard = []
        for rowIDX in range(10):
            tmp = {}
            tmp['rank'] = tuples[rowIDX]['rank']
            tmp['song'] = tuples[rowIDX]['song']
            tmp['artist'] = tuples[rowIDX]['artist']
            sql = "select weight, date, time from api_total where song=%s"
            params = (tmp['song'])
            util = DB_Utils()
            weights = util.queryExecutor(db=config('DB_NAME'), sql=sql, params=params)
            date_list = []
            time_list = []
            weights_list = []
            for idx in range(len(weights)):
                date_list.append(weights[idx]['date'])
                time_list.append(weights[idx]['time'])
                weights_list.append(weights[idx]['weight'])
            tmp['date'] = date_list[len(date_list)-49:]
            tmp['time'] = time_list[len(time_list)-49:]
            tmp['weight'] = weights_list[len(weights_list)-49:]
            dashboard.append(tmp)
        return dashboard

