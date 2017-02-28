from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from blog import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from markdown import markdown
from django.core.urlresolvers import reverse_lazy
from datetime import datetime

#
# class IndexView(ListView):
#     template_name = 'blog/index.html'
#     context_object_name = 'articles_list'
#
#     def get_queryset(self):
#         return models.Articles.objects.all()[:5:-1]  # 倒序，5个；

def blog_index(request):
   articles_list =  models.Articles.objects.all().order_by('-mod_time')[:5]  # 倒序，5个；
   comments_list = models.Comments.objects.all().order_by('-pub_time')[:5]  # 倒序，5个；

   return render(request,
                 'blog/index.html',
                 {
                     "articles_list":articles_list,
                     "comments_list":comments_list,
                 })



# class ArticleDetailView(DetailView):
#     model = models.Articles
#     template_name = 'blog/detail.html'
def _comments_sort(comments):
    '''
    按照显示顺序进行排序
    :param comments: obj列表
    :return:返回排序后的评论
    '''
    comments_ret = []
    comments_level_list = []
    for comment in comments:
        if not comment.upper_comments:
            comments_ret.append(comment)
            comments_level_list.append(0)

        else:
            comment_index = comments_ret.index(comment.upper_comments)
            comment_level = comments_level_list[comment_index] + 30
            comments_ret.insert(comment_index+1, comment)
            comments_level_list.insert(comment_index+1, comment_level)
    return list(zip(comments_ret,comments_level_list))

def article_detail(request,article_id):
    articles = models.Articles.objects.get(id=article_id)
    comments = articles.comments_set.all().order_by('pub_time')
    comments = _comments_sort(comments)  # 特殊排序
    return render(request,
                  'blog/detail.html',
                  {"articles":articles,
                   "comments":comments,
                   }
                  )


def comments_add(request,article_id,comments_id=None):

    if request.method == "POST":
        print(request.POST)
        vister = request.POST.get('vister')
        title = request.POST.get('title')
        pub_time = datetime.now()
        article = models.Articles.objects.get(id=article_id)
        upper_comments_id = request.POST.get('comment_id')
        if upper_comments_id:
            upper_comments_id = int(upper_comments_id.split('-')[-1])
            upper_comments = models.Comments.objects.get(id=upper_comments_id)
        else:
            upper_comments = None
        content = request.POST.get('content')

        new_comment = models.Comments(
            vister=vister,
            title=title,
            pub_time=pub_time,
            article=article,
            upper_comments= upper_comments,
            content=content
        )
        new_comment.save()
    return HttpResponseRedirect(reverse_lazy('blog:detail',args=[article_id]))


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

