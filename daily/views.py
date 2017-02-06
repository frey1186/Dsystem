from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request): # 首页测试
    return HttpResponse('ok.')