from django.shortcuts import render#,redirect,HttpResponse
from django.contrib import auth
#from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.
from . import models
from django.views.decorators.csrf import ensure_csrf_cookie
#from django.views.decorators.csrf import csrf_exempt
import os
import json
import time
import uuid
from cdb.settings import BASE_DIR
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from . import  serializers
from rest_framework import pagination

#自定义认证类
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
class MyAuth(BaseAuthentication):
    def authenticate(self,request):
        token = request.query_params.get('token','')
        if not token:
            raise AuthenticationFailed('缺少token 格式：pathname/?token=uuid')
        user = models.UserInfo.objects.filter(token=token).first()
        if not user:
            raise AuthenticationFailed('token不合法')
        return (user,token) #request.user & request.auth

def index(request):
    return render(request, "index.html")

#注册
class User_register(APIView):
    def get(self, request):
        return Response({"detail": '登录接口只开放POST请求,格式（英文标点）：{“username”:“古川”,“password”:“123456”}'})
    def post(self, request):  # {"username":"古川","password":"123456"}
        username=request.data.get("username",'').strip()
        if not models.UserInfo.objects.filter(username=username):
            password=request.data.get("password",'').strip()
            try:
                user = models.UserInfo.objects.create_user(username=username,password=password)
                user_obj = dict()
                user_obj['msg'] = user.id
                user_obj['token'] = user.token
            except:
                return Response({"msg": 0, "detail": '密码不合要求'})  # 密码不合要求
            else:
                return Response(user_obj)  # 注册成功
        return Response({"msg": 0, "detail": "用户名已经被占用" })  # 注册失败 用户名已经被占用

#登录
class LoginView(APIView):
    def get(self,request):
        return Response({"detail":'登录接口只开放POST请求,格式（英文标点）：{“username”:“古川”,“password”:“123456”}'})
    def post(self,request):#{"username":"古川","password":"123456"}
        username = request.data.get("username",'')
        password = request.data.get("password", '')
        user = auth.authenticate(username=username, password=password)
        user_obj = dict()
        if user:
            auth.login(request,user)
            user.token = uuid.uuid4()
            user.save()
            user_obj['msg'] = user.id
            user_obj['token'] = user.token
            return Response(user_obj)
        user_obj['msg'] = 0
        return Response(user_obj)

#验证登录状态
class User_is_login(APIView):
    authentication_classes = [MyAuth,]
    def get(self,request):
        user_obj = dict()
        user_obj['msg'] = request.user.id
        user_obj['token'] = request.auth
        return Response(user_obj)


#注销登录
class User_logout(APIView):
    authentication_classes = [MyAuth, ]
    def get(self,request):
        request.user.token=''
        request.user.save()
        return Response({"msg":1})  #注销成功


#相册列表页
def picture(request):
    album_list = models.Album.objects.all()
    return render(request, "picture.html", {"album_list": album_list})

#相册详情页
def picture_watch(request):
    album_id = request.GET.get("albumId")
    album = models.Album.objects.get(id=album_id)
    return render(request, "picture_watch.html", {"album": album})

#上传相册表单示例
def add_album_form(request):
    token=request.user.token
    return render(request, "relaxation_addAlbum.html",{'token':token})

#上传相册接口
class Add_album(APIView):
    authentication_classes = [MyAuth,]
    def get(self,request):
        return Response({"detail":'上传接口只开放POST请求,推荐使用表单对象上传,file类型的键名请用file0 - file8'})
    def post(self,request):
        title=request.data.get("title",'')
        user_id = request.user.id
        motif = request.data.get("motif",'').strip()
        length = request.data.get("length",'')
        if request.FILES.get("file0") is None:
            return Response({"msg": 0,"detail": '上传失败 无文件'})
        if int(length)<1 or int(length)>9:
            return Response({"msg": 0,"detail": '上传失败 文件个数不匹配'})
        try:
            imgurl_list=[]
            for i in range(int(length)):
                file_obj = request.FILES.get('file'+str(i))
                #给图片拼接静态目录路径，并去掉图片文件名中可能含有的百分号。
                imgurl = os.path.join('static', 'picture','img', str(int(time.time()+i))+file_obj.name.replace("%",""))
                imgurl_list.append(imgurl)
                f = open(os.path.join(BASE_DIR, imgurl), 'wb')
                for chunk in file_obj.chunks():
                    f.write(chunk)
                f.close()
        except:
            return Response({"msg": 0,"detail": '储存过程失败 可以反馈给程序猿'})#(一个chunk：2.5M)
        else:
            imgurl_list_json = json.dumps(imgurl_list)
            models.Album.objects.create(title=title, imgurl=imgurl_list_json,imglen=length, motif=motif, publisher_id=user_id)
            return Response({"msg": 1})#发表成功

#自定义分页类
class MyPageNumberPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = "size"
    max_page_size = 10
    page_query_param = "page"




class AlbumView(viewsets.ModelViewSet):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializers

    pagination_class = MyPageNumberPagination
