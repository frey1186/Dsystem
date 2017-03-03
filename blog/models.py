from django.db import models
from django.core.urlresolvers import reverse
from user.models import UserProfile

# Create your models here.

class Tag(models.Model):
    name = models.CharField('标签',max_length=32)
    brief = models.CharField('摘要',max_length=32,blank=True,null=True)

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField('文章',max_length=128,)
    # author = models.ForeignKey(UserProfile,verbose_name='作者',blank=True)
    content = models.TextField('内容')
    mod_time = models.DateField('修改时间',auto_now=True)
    type_choice = (
        (1,'原创'),
        (2,'转载'),
        (3,'翻译'),
    )
    article_type = models.IntegerField('文章类型',choices=type_choice,default=1)
    tags = models.ManyToManyField('Tag',blank=True)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'article_id': self.pk})

    class Meta:
        ordering = ['-mod_time']

    def __str__(self):
        return self.title



class Comments(models.Model):
    vister = models.CharField('访客', max_length=16)
    pub_time = models.DateTimeField(u'评论时间', auto_now_add=True)
    title = models.CharField('标题',max_length=128, blank=True, null=True)
    upper_comments = models.ForeignKey('self',
                                        related_name="lower_comments",
                                        blank=True,null=True)
    article = models.ForeignKey(Articles)
    content = models.TextField('评论')
    user_agent = models.CharField('浏览器',max_length=16,blank=True,null=True)
    remote_host = models.CharField('客户端地址',max_length=16,blank=True,null=True)

    def __str__(self):
        return '%s-%s comment at %s' % (self.id, self.vister, self.pub_time)

