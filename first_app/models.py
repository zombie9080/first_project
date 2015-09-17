#!/bin/python
# -*- encoding=utf-8 -*- #


from django.db import models

class Mysite(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    author = models.CharField(max_length=100)
    num = models.IntegerField()
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['num']  # 每次都按照 num 排序

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=30)
    qq = models.CharField(max_length=15)
    def __unicode__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    def __unicode__(self):
        return self.title
