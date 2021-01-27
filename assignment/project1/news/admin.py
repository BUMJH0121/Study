from django.contrib import admin
from news.models import News
# Register your models here.

class ItNewsAdmin(admin.ModelAdmin):
    list_display = ('kind','title')
    
admin.site.register(News, ItNewsAdmin)