from django.conf.urls import url
from tfMaker import views


urlpatterns = [
    url(r'^$', views.index, name='index'),  # 首页
]
