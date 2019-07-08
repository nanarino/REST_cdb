from django.db import models
from django.contrib.auth.models import AbstractUser

__all__=['Album',]

#ORM相关
class UserInfo(AbstractUser):
    qq = models.CharField(max_length=11)
    token = models.UUIDField(null=True,blank=True)

class Album(models.Model):
    id = models.AutoField(primary_key=True)#创建自增主键字段
    title = models.CharField(max_length=14,default="无题") #创建一个varchar类型的不可为空字段
    imgurl = models.TextField(max_length=64)
    imglen = models.CharField(max_length=2)
    motif = models.CharField(max_length=14,default="未分类")
    time = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(to="UserInfo")
    def __repr__(self):
        return "<{}-{}>".format(self.title,self.motif)
    #drf排序依据
    class Meta:
        ordering = ('id',)