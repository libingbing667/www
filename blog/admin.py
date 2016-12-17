#-*- coding:utf-8 -*-
from django.contrib import admin
from models import *


class ArticleAdmin(admin.ModelAdmin):

    #fields = ('title','desc','content')
    list_display = ('title','desc','click_count')
    list_display_links = ('title', 'desc', 'click_count')




# Register your models here.

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Catagory)
admin.site.register(Comment)
admin.site.register(Link)
admin.site.register(Ad)
