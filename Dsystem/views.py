from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


def user_login(request):
    if request.method == "POST":
        print("post:",request.POST)
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next') or reverse("blog:index"))
        else:
            login_err = "Wrong username or password!"
            return render(request, 'user_login.html', {'login_err': login_err})
    return render(request, 'user_login.html')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))




def home(request):

    if  request.user.is_authenticated(): # 判断是否已经登录用户
        return render(request,'base.html')
    else:
        return HttpResponseRedirect(reverse("login"))
