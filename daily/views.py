from django.shortcuts import render,HttpResponse
from django.shortcuts import HttpResponseRedirect
from daily import forms
from datetime import datetime,date
from django.core.urlresolvers import reverse
from daily import models
# Create your views here.


def index(request): # 首页测试
    return render(request, 'daily/index.html')



def add_daily(request):


    # TODO: 分类不选就保存，不会返回错误消息

    form = forms.DailyModelForm()
    # 创建一个空表单
    context = {"form":form}
    try:
        if request.method == "POST":
            form = forms.DailyModelForm(request.POST)  # 将POST内容填入表单
            print(request.POST)

            # todo: 前端判断工作时间
            # 判断工作时间是否超过24小时 --应该在前端判断
            # if float(request.POST.get('hours')) >=24:
            #     context['err'] = "亲，工作时间太他妈长了。"
            #     return render(request, "daily/add_daily.html", context)

            if form.is_valid():
                new_daily = form.save(commit=False)
                now = datetime.now()
                new_daily.upload_date = date(now.year, now.month, now.day)
                new_daily.user = request.user.userprofile
                new_daily.status = 1
                new_daily.comment = ''
                new_daily.save()
                form.save_m2m()
                return HttpResponseRedirect(reverse('daily:history'))
        return render(request,"daily/add_daily.html",context)

    except Exception as e:
        print(e)
        context['err'] = "亲，你今天已经填写过日报了。"
        return render(request,"daily/add_daily.html",context)


def history(request):
    daily_history = models.Daily.objects.filter(user=request.user.userprofile)
    return render(request, 'daily/history.html',{"history":daily_history})