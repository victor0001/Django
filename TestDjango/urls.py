from django.conf.urls import patterns, include, url
from TestDjango.blog.views import archive,home,getArticles
from TestDjango.blog.bolgAjax import showArticle,addComment,favorAdd

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', home),
    # url(r'^TestDjango/', include('TestDjango.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^archive/',archive),
    url(r'^blog/(?P<articleId>[0-9]+)/',showArticle),
    url(r'^blog/addcomment/(?P<articleId>[0-9]+)/',addComment),
    url(r'^favor/',favorAdd),
    url(r'^getarticles/',getArticles)
)
