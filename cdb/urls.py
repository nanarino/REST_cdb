"""cdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from nanarino import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/albums/$', views.AlbumView.as_view({"get":"list"})),
    url(r'^api/album/(?P<pk>\d+)/$', views.AlbumView.as_view({"get":"retrieve"})),
    url(r'^picture/$', views.picture),
    url(r'^picture/watch/$', views.picture_watch),
    url(r'^addAlbum/$', views.Add_album.as_view()),
    url(r'^addAlbumForm/$', views.add_album_form),
    url(r'^user/login/$', views.LoginView.as_view()),
    url(r'^user/logout/$', views.User_logout.as_view()),
    url(r'^user/register/$', views.User_register.as_view()),
    url(r'^user/isLogin/$', views.User_is_login.as_view()),
    url(r'^$', views.index),
]
