from django.utils.deprecation import MiddlewareMixin

class DisableCSRFCheck(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)

"""
class AlbumListView(APIView):
    #authentication_classes = [auth.MyAuth, ]
    def get(self,request):
        auth.MyAuth().authenticate(request=request)
        pass
在get请求中 直接实例化认证类执行方法 和 类级声明认证类等效


class AlbumListView(APIView):
    #authentication_classes = [auth.MyAuth, ]
    def post(self,request):
        auth.MyAuth().authenticate(request=request)
        pass

而在post请求中想直接实例化认证类执行方法来代替类级声明会导致403
原因是drf其内部重载了django里面的csrf middleware，
而且没发现有地方可以关掉这个功能，
即使在django里面去掉这个middleware，但是这个还是会调用的。
"""

#本中间件的作用就是强制绕过csrf middleware