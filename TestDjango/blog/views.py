# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from django.db import connection
from TestDjango.blog.models import article,comment, category
def archive(request):
    articles = article.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'model':articles})
    return HttpResponse(t.render(c))

def home(request):
    latestArticles = article.objects.order_by("-addDate").order_by("-addTime")[0:5]
    totalCount = len(article.objects.all())
    results = []
    for blog in latestArticles:
        comments = comment.objects.filter(article_id=blog.id)
        results.append({"article":blog,"commentCount":comments.count()})
    categoryList = category.objects.all()
    popArticles = article.objects.order_by("-favorcount")[0:5]
    t = loader.get_template("articleInIndex.html")
    c = Context({'model':results,"categoryList":categoryList,"popArticles":popArticles,"totalCount":totalCount})
    return HttpResponse(t.render(c))


def getArticles(request):
    postData = request.POST
    pageIndex = int(postData["pageIndex"])
    pageCount = int(postData["pageCount"])
    artIndex = pageIndex * pageCount
    articles = article.objects.order_by("-addDate").order_by("-addTime")[artIndex:artIndex + 5]
    results = []
    for blog in articles:
        comments = comment.objects.filter(article_id=blog.id)
        results.append({"article":blog,"commentCount":comments.count()})
    t = loader.get_template("ArticleList.html")
    c = Context({'model':results})
    return HttpResponse(t.render(c))

    
