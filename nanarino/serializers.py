from rest_framework import serializers
from nanarino.models import UserInfo,Article,Album,Comment,Staff
import json

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id', 'username')

class ArticleListSerializers(serializers.ModelSerializer):
    writer = UserSerializers(read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'motif', 'time', 'writer')

class ArticleSerializers(serializers.ModelSerializer):
    writer = UserSerializers(read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'motif', 'content', 'time', 'writer')


class AlbumListSerializers(serializers.ModelSerializer):
    publisher = UserSerializers(read_only=True)
    class Meta:
        model = Album
        fields = ('id', 'title', 'motif', 'imglen', 'time', 'publisher')


class AlbumSerializers(serializers.ModelSerializer):
    publisher = UserSerializers(read_only=True)
    imglist = serializers.SerializerMethodField()
    def get_imglist(self, obj):
        return json.loads(obj.imgurl)
    class Meta:
        model = Album
        fields = ('id', 'title', 'motif', 'imglen', 'time', 'publisher','imglist')


class CommentListSerializers(serializers.ModelSerializer):
    writer = UserSerializers(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'time', 'writer')