from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from . import  models,serializers,pagination,auth
from django.contrib.auth import authenticate,login,logout
#from rest_framework import viewsets
import os,json,time,uuid
from REST_cdb.settings import BASE_DIR

def index(request):
    return render(request, "index.html")


#注册
class RegisterView(APIView):

    def get(self, request):
        return Response({"detail": "注册接口只开放POST请求,格式（英文标点）","例如":{"username":"古川","password":"123456"}})

    def post(self, request):
        username=request.data.get("username",'').strip()
        if not models.UserInfo.objects.filter(username=username):
            password=request.data.get("password",'').strip()
            try:
                user = models.UserInfo.objects.create_user(username=username,password=password)
                user_obj = dict()
                user_obj['msg'] = user.id
                user_obj['token'] = "请再次登录获取"
            except:
                return Response({"msg": 0, "detail": '密码不合要求'})  # 密码不合要求
            else:
                return Response(user_obj)  # 注册成功
        return Response({"msg": 0, "detail": "用户名已经被占用" })  # 注册失败 用户名已经被占用

#登录
class LoginView(APIView):

    def get(self,request):
        return Response({"detail": "登录接口只开放POST请求,格式（英文标点）","例如":{"username":"古川","password":"123456"}})

    def post(self,request):
        username = request.data.get("username",'')
        password = request.data.get("password", '')
        user = authenticate(username=username, password=password)
        user_obj = dict()
        if user:
            login(request,user)
            user.token = uuid.uuid4()
            user.save()
            user_obj['msg'] = user.id
            user_obj['token'] = user.token
            return Response(user_obj)
        user_obj['msg'] = 0
        user_obj["detail"] = "用户名或密码错误"
        return Response(user_obj)

#注销登录
class LogoutView(APIView):
    authentication_classes = [auth.MyAuth, ]
    def get(self,request):
        request.user.token=None
        request.user.save()
        try:
            if request.user.is_authenticated():
                logout(request)
        except Exception:
            pass
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


class AlbumListView(APIView):
    #authentication_classes = [auth.MyAuth, ]
    def get(self,request):
        # auth.MyAuth().authenticate(request=request)
        qs = models.Album.objects.all()
        pg = pagination.MyPageNumberPagination()
        pg_qs = pg.paginate_queryset(queryset=qs,request=request,view=self)
        sl = serializers.AlbumListSerializers(instance=pg_qs,many=True)
        return pg.get_paginated_response(sl.data)

    def post(self,request):
        auth.MyAuth().authenticate(request=request)
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
            return Response({"msg": 0,"detail": '储存过程失败 可以反馈给程序猿'})#一个chunk：2.5M
        else:
            imgurl_list_json = json.dumps(imgurl_list)
            models.Album.objects.create(title=title, imgurl=imgurl_list_json,imglen=length, motif=motif, publisher_id=user_id)
            return Response({"msg": 1})#发表成功

class AlbumView(APIView):
    def get(self,request,pk):
        qs = models.Album.objects.filter(id=pk)
        sl = serializers.AlbumSerializers(instance=qs,many=True)
        return Response(sl.data)
