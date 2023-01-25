from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def insert_topic(request):
    tn=input('enter topic name')
    T=topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('topic data is inserted successfully')

def insert_webpage(request):
    tn=input('enter topic name')
    name=input('enter name')
    url=input('enter url')
    T=topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse('webpage is inserted ')

def insert_records(request):
    tn=input('enter topic name')
    name=input('enter name')
    url=input('enter url')
    date=input('enter date')
    A=accessrecords.objects.get_or_create(topic_name=tn,name=name,url=url,date=date)[0]
    A.save()
    return HttpResponse('records inserted successfully')