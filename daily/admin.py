from django.contrib import admin
from daily import  models
# Register your models here.



class UserProfileAdmin(admin.ModelAdmin):


    fieldsets = [
        ('Name',               {'fields': ['name','user']}),
        ('Basic information', {'fields': ['signature','head_portrait']}),
    ]




admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Daily)
admin.site.register(models.Categories)