from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
import json
from django.core import serializers
import time, os
from datetime import datetime
import requests
from django.db.models import Count
import time
from datetime import date


# Chart data
@api_view(['POST'])
def y_data_ts_1(request):
    print("function y_data_ts_1 is running")
    today = date.today()
    seven_day=[]
    for i in [7,6,5,4,3,2,1,0]:
        seven_days=date(today.year, today.month, today.day-i)
        seven_day.append(seven_days)
    chart = request.data["chart"]
    data1= y_data_ts.objects.all()
    data2=[]
    for i in seven_day:
        result=data1.filter(date=i)
        if(len(result)):
          data2.extend(result)
    data5=[]
    for n in data2:
        # set_data=[]
        # for i in n:
            temp=[n.time,n.data]
            # set_data.append(temp)
            data5.append(temp)
    # print("data55555555555",data5)
    
    final_date=[]
    data_final=[]
    
    # print('dataa',data5)

    for n in data5:
        # for i in n:
           
            date_initial=n[0]
            pattern = '%Y-%m-%d %H:%M:%S'
            epoch = int(time.mktime(time.strptime(date_initial, pattern)))
            # print("iiiiiiiiii",n[0])
            n[0] = epoch*1000   
            if n[1]!=None:
              n[1] = float(n[1])       
    # print("fina_data",data5)
    return Response(data5)

def y_data_1(request):
    print("function y_data_1 is running")
    chart = request.data["chart"]
    yahoo_obj = yahoo_data.objects.all().filter(chart = chart , chart_type = "1week")
    data = []
    for n in yahoo_obj:
        temp= [n.date, n.data]
        data.append(temp)
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        for j in data:
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        date = i[0] ##+ " 00:00:00"
        pattern = '%m-%d-%Y' # %H:%M:%S'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    return Response(final_data)


@api_view(['POST'])
def y_data_2(request):
    chart = request.data["chart"]
    yahoo_obj = yahoo_data.objects.all().filter(chart = chart , chart_type = "1month")
    data = []
    for n in yahoo_obj:
        temp= [n.date, n.data]
        data.append(temp)
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        for j in data:
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        date = i[0] #+ " 00:00:00"
        pattern = '%m-%d-%Y' # %H:%M:%S'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    return Response(final_data)

@api_view(['POST'])
def y_data_3(request):
    chart = request.data["chart"]
    yahoo_obj = yahoo_data.objects.all().filter(chart = chart , chart_type = "3month")
    data = []
    for n in yahoo_obj:
        temp= [n.date, n.data]
        data.append(temp)
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        for j in data:
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        date = i[0] #+ " 00:00:00"
        pattern = '%m-%d-%Y' # %H:%M:%S'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    return Response(final_data)

@api_view(['POST'])
def y_data_4(request):
    chart = request.data["chart"]
    yahoo_obj = yahoo_data.objects.all().filter(chart = chart , chart_type = "6month")
    data = []
    for n in yahoo_obj:
        temp= [n.date, n.data]
        data.append(temp)
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        for j in data:
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        date = i[0] #+ " 00:00:00"
        pattern = '%m-%d-%Y' # %H:%M:%S'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    return Response(final_data)

@api_view(['POST'])
def y_data_5(request):
    chart = request.data["chart"]
    yahoo_obj = yahoo_data.objects.all().filter(chart = chart , chart_type = "1year")
    data = []
    for n in yahoo_obj:
        temp= [n.date, n.data]
        data.append(temp)
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        for j in data:
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        date = i[0] #+ " 00:00:00"
        pattern = '%m-%d-%Y' # %H:%M:%S'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    return Response(final_data)

@api_view(['POST'])
def y_data_6(request):
    chart = request.data["chart"]
    yahoo_obj = yahoo_data.objects.all().filter(chart = chart , chart_type = "2year")
    data = []
    for n in yahoo_obj:
        temp= [n.date, n.data]
        data.append(temp)
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        for j in data:
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        date = i[0] #+ " 00:00:00"
        pattern = '%m-%d-%Y' # %H:%M:%S'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    return Response(final_data)
