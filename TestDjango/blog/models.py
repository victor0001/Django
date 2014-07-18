from django.db import models
from django.contrib import admin
from django.shortcuts import render_to_response

class category(models.Model):
    title = models.CharField(max_length=50)
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title

#Article table
class article(models.Model):
    title = models.CharField(max_length=50)
    abstract = models.CharField(max_length=300)
    content = models.TextField()
    addDate = models.DateField()
    addTime = models.TimeField()
    modifiedDate = models.DateField()
    modifiedTime = models.TimeField()
    keywords = models.CharField(max_length=50)
    favorcount = models.PositiveIntegerField()
    #publish=models.BooleanField()
    category=models.ForeignKey(category)
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title

#Comments table
class comment(models.Model):
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    article = models.ForeignKey(article)
    addTime=models.DateTimeField()
    #publish=models.BooleanField()
    def __unicode__(self):
        return self.subject
    def __str__(self):
        return self.subject

# Create your models here.
