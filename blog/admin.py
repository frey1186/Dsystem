from django.contrib import admin

# Register your models here.
from blog import models


admin.site.register(models.Articles)
admin.site.register(models.Tag)
admin.site.register(models.Comments)