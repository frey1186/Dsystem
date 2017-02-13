from django.db import models
from blog.models import Articles
# Create your models here.

class Comments(models.Model):
    vister = models.CharField('访客', max_length=16)
    pub_time = models.DateTimeField(u'评论时间', auto_now_add=True)
    title = models.CharField('标题',max_length=128, blank=True, null=True)
    upper_comments = models.ManyToManyField('self',
                                        related_name="lower_comments",
                                        blank=True)
    article = models.ForeignKey(Articles)
    content = models.TextField('评论')

    def __str__(self):
        return '%s-%s comment at %s' % (self.id, self.vister, self.pub_time)


