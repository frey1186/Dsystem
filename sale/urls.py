from django.conf.urls import url
from sale import views


urlpatterns = [
    url(r'^$', views.sale_index, name='index'),  # 首页



    # url(r'^archive/$', views.archive, name='archive'),  # 文章归档
    # # url(r'^(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),  # 详细信息
    # url(r'^(?P<article_id>[0-9]+)/$', views.article_detail, name='detail'),  # 详细信息
    # url(r'^(?P<article_id>[0-9]+)/comments/add/$', views.comments_add, name='comments-add'),  # add comments
    #
    # url(r'^add/$', views.NewArticlelView.as_view(), name='article-add'),  # 新增文章
    # url(r'^(?P<pk>[0-9]+)/update/$', views.ArticleUpdateView.as_view(), name='article-update'),  # change
    # url(r'^(?P<pk>[0-9]+)/delete/$', views.ArticleDeleteView.as_view(), name='article-delete'),  # delete article

]
