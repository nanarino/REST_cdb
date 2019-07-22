#自定义认证类
from . import  models
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