from django.shortcuts import render_to_response
from TestDjango.blog.models import article,comment,category
from django.db import connection
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from datetime import datetime
def showArticle(request,articleId="1"):
    curArticle = article.objects.get(id=articleId)
    comments=comment.objects.filter(article=curArticle)
    categoryList=category.objects.all()
    popArticles=article.objects.order_by("-favorcount")[0:5]
    c=RequestContext(request,{'model':curArticle,'comments':comments,"categoryList":categoryList,"popArticles":popArticles})
    return render_to_response("blogArticle.html",c)

def addComment(request,articleId="1"):
    postData=request.POST
    curArticle = article.objects.get(id=articleId)
    newComment = comment()
    newComment.addTime=datetime.now()
    newComment.email=postData["email"]
    newComment.article=curArticle
    newComment.subject=postData["subject"]
    newComment.message=postData["message"]
    newComment.save()
    return HttpResponseRedirect("/blog/"+articleId)

def favorAdd(request):
    postData=request.POST
    articleId=postData["articleId"]
    count=int(postData["count"])
    curArticle=article.objects.get(id=articleId)
    curArticle.favorcount+=count
    curArticle.save()
    return HttpResponse("")