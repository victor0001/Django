from TestDjango.blog.models import article,comment
#from django.db import models
from django.contrib import admin

class commentsInline(admin.TabularInline):
    model = comment
    extra = 1
    max_num = 5

class article_admin(admin.ModelAdmin):
    list_display = ('id','title','addDate')
    fields=("title","abstract","content","category",("addDate","addTime"),("modifiedDate","modifiedTime"),"keywords","favorcount")
    inlines = [commentsInline]
    #def add_view(self,request,form_url='',extra_content=None):
    #    return super(self).add_view(request,form_url,extra_content)
admin.site.register(article,article_admin)
