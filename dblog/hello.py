# coding=UTF-8
from django.http import HttpResponse
from  django.shortcuts import render_to_response

address = [{'name': '张三', 'address': '地址一'}, {'name': '李四', 'address': '地址二'}]


def index(request):
    return render_to_response('index.html', {'address': address})


def hello(request):
    return HttpResponse("Hello, Django.")


def echo(request):
    print  request
    #print msg
    return HttpResponse("Hello, Django.")
