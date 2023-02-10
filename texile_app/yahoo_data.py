from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
import json
from django.core import serializers
import time, os
import datetime
import requests
from django.db.models import Count
import time
from datetime import date
import math
from calendar import monthrange
from django.db.models import Q
# Chart data
@api_view(['POST'])
def y_data_ts_1(request,duration,country):
    print("function y_data_ts_1 is running",duration)
    chart = request.data["chart"]
    print("couuntryyy",country)
    #####Duration is the interval in minute within which the user wants the periodic data
    ### As data is coming for every 5 minutes therefore user should give a duration of 5 or above, 
    ###### in case duration is below 5 then it will automatically be conerted to 5
    if(duration<5):
        duration=5
    ### After every 5 minute data is being updated
    ### Therefore duration devided by 5 will give the interval 
    ### Let suppose user wants data after every 20 minutes, then 20/5=4;
    ### Hence in every 4th position we have the data for time interval of 20 mins
    interval=math.trunc(duration/5)
    seven_day=[]
    today = date.today()
    day=today.day
    month=today.month
    year=today.year
    final_day=today.day
    if(day<=7):
        month=month-1
        num_days = monthrange(year, month)[1]
        days_extra=7-day
        final_day=num_days-days_extra
    else:
        final_day=day-7
    if(month>12):
        month=1
        year=year+1
    date_7_days_ago=datetime.datetime(year, month,final_day , 9,0 ,0)
    dataAnonymous=[]
    queySet=[]
    dataUTC=[]
    data1=[]
    data2=[]
    for i in range (0,7):
        print(i)
        # if(country=='America'):
        #     minTime=date_7_days_ago=datetime.datetime(year, month,final_day+i , 14,30 ,0)
        #     maxTime=date_7_days_ago=datetime.datetime(year, month,final_day+i, 21,0 ,0)
        #     data123=hourly_yahoo_data.objects.filter(Q(update_time__gte=minTime)&Q(update_time__lte=maxTime)&Q(chart = chart))
        #     dataUTC.extend(data123)
        if(country=='America'):
            minTime=date_7_days_ago=datetime.datetime(year, month,final_day+i , 14,30 ,0)
            maxTime=date_7_days_ago=datetime.datetime(year, month,final_day+i, 21,0 ,0)
            data123=hourly_yahoo_data.objects.filter(Q(update_time__gte=minTime)&Q(update_time__lte=maxTime)&Q(chart = chart))
            print("heeey")
            dataUTC.extend(data123)
        if(country=='Japan'):
            minTime=date_7_days_ago=datetime.datetime(year, month,final_day+i , 0,0 ,0)
            maxTime=date_7_days_ago=datetime.datetime(year, month,final_day+i, 6,0 ,0)
            data12=hourly_yahoo_data.objects.filter(update_time__gte=minTime,update_time__lte=maxTime,chart = chart)
            dataUTC.extend(data12)
        if(country=='Paris'):
            minTime=date_7_days_ago=datetime.datetime(year, month,final_day+i , 8,0 ,0)
            maxTime=date_7_days_ago=datetime.datetime(year, month,final_day+i, 16,30 ,0)
            dataParis=hourly_yahoo_data.objects.filter(update_time__gte=minTime,update_time__lte=maxTime,chart = chart)
            dataUTC.extend(dataParis)

    if(country!='Paris'and country!='America'and country!='Japan'):
      dataAnonymous=hourly_yahoo_data.objects.filter(update_time__gte=date_7_days_ago,chart = chart )
    print("hhhey",(dataUTC))
    if(len(dataUTC)):
     data1=dataUTC
    elif(len(dataAnonymous)):
        data1=dataAnonymous
  
     
    # print(data2)

    # #### To fetch data of the specified interval we are running a simple for loop 
    for i in range(1,len(data1)-1):
        if(i!=0):
            if((i+1)%interval==0):
                data2.append(data1[i])
    # print(len(data2),data2[0])
    #######################Uncomment##################
    data5=[]
    for n in data2:
        # set_data=[]
        # for i in n:
            temp=[n.update_time,n.val]
            # set_data.append(temp)
            data5.append(temp)
    # print("data55555555555",data5)

    final_date=[]
    data_final=[]
    
    # print('dataa',data5)

    for n in data5:
        # for i in n:
           
            date_initial=n[0]
            pattern = '%Y-%m-%d %H:%M:%S.%f'
            ###### To covert time in milliseconds
            epoch = int(time.mktime(time.strptime(date_initial, pattern)))
            # print("iiiiiiiiii",n[0])
            n[0] = epoch*1000   
            if n[1]!=None:
              n[1] = float(n[1])       
    # print("fina_data",data5)
    return Response(data5)
@api_view(['POST'])
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

    date.sort(key = lambda date: datetime.datetime.strptime(date, '%m-%d-%Y'))
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

    date.sort(key = lambda date: datetime.datetime.strptime(date, '%m-%d-%Y'))
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

    date.sort(key = lambda date: datetime.datetime.strptime(date, '%m-%d-%Y'))
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

    date.sort(key = lambda date: datetime.datetime.strptime(date, '%m-%d-%Y'))
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

    date.sort(key = lambda date: datetime.datetime.strptime(date, '%m-%d-%Y'))
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

    date.sort(key = lambda date: datetime.datetime.strptime(date, '%m-%d-%Y'))
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
