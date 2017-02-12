from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),  # 首页
    url(r'^(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),  # 详细信息
    url(r'^add/$', views.NewArticlelView.as_view(), name='article-add'),  # 新增文章
    url(r'^(?P<pk>[0-9]+)/update/$', views.ArticleUpdateView.as_view(), name='article-update'),  # change
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ArticleDeleteView.as_view(), name='article-delete'),  # delete article

]
