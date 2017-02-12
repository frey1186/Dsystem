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
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-mod_time']

    def __str__(self):
        return self.title


