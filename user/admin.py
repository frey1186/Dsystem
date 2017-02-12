from django.contrib import admin
from user import models
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):


    fieldsets = [
        ('Name',               {'fields': ['name','user']}),
        ('Basic information', {'fields': ['signature',]}),
    ]




admin.site.register(models.UserProfile, UserProfileAdmin)