from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

__all__=['Article','Album','Comment','Staff']


class UserInfo(AbstractUser):
    qq = models.CharField(max_length=11)
    token = models.UUIDField(null=True, blank=True)

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False,max_length=14)
    content = models.TextField(null=False,max_length=2000)
    motif = models.CharField(null=True,max_length=14)
    time = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(to="UserInfo")
    def __repr__(self):
        return "<{}-{}>".format(self.title,self.motif)
    class Meta:
        ordering = ('time',)

class Album(models.Model):
    id = models.AutoField(primary_key=True)#创建自增主键字段
    title = models.CharField(null=False,max_length=14)
    imgurl = models.TextField(null=False,max_length=64)
    imglen = models.CharField(null=False,max_length=2)
    motif = models.CharField(null=True,max_length=14)
    time = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(to="UserInfo")
    def __repr__(self):
        return "<{}-{}>".format(self.title,self.motif)
    class Meta:
        ordering = ('time',)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(null=False,to="Article")
    album = models.ForeignKey(null=False,to="Album")
    writer = models.ForeignKey(null=False,to="UserInfo")
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=128)
    def __repr__(self):
        return "<{}>".format(self.content)
    class Meta:
        ordering = ('time',)

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, max_length=14)
    content = models.TextField(null=False, max_length=2000)
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('time',)