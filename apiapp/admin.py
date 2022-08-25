from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import NewsID, News


class HackerNewsIDAdmin(admin.ModelAdmin):
    list_display = ('hackernews', 'time') #these are the features to be listed
    list_display_links = ('hackernews', 'time') #these are the features links

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'time') #these are the features to be listed
    list_display_links = ('title', 'time') #these are the features links

admin.site.register(NewsID, HackerNewsIDAdmin)
admin.site.register(News, NewsAdmin)
