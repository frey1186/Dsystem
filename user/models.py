from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.


class UserProfile(models.Model):
    '''
    用户相关
    '''
    user = models.OneToOneField(User)
    name = models.CharField(u'姓名', max_length=16, )
    signature = models.CharField(u'个性签名', max_length=255,
                                 blank=True, null=True)


    def __str__(self):
        return self.user.username












