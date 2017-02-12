from django.shortcuts import render,HttpResponse
from blog import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from markdown import  markdown
from django.core.urlresolvers import reverse_lazy


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'articles_list'

    def get_queryset(self):
        return models.Articles.objects.all()[:5:-1]  # 倒序，5个；



class ArticleDetailView(DetailView):
    model = models.Articles
    template_name = 'blog/detail.html'


class NewArticlelView(CreateView):
    model = models.Articles
    fields = '__all__'

    class Media:
        css = {
            'all': ('/static/bootstrap/css/blog.css',)
        }


class ArticleUpdateView(UpdateView):
    model = models.Articles
    fields = '__all__'

class ArticleDeleteView(DeleteView):
    model = models.Articles
    success_url = reverse_lazy('blog:index')

