from django.contrib import admin
from daily import  models
# Register your models here.



class UserProfileAdmin(admin.ModelAdmin):
    pass








admin.site.register(models.UserProfile)
admin.site.register(models.Daily)
admin.site.register(models.Categories)