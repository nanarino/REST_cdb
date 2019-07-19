from rest_framework import serializers
from nanarino.models import UserInfo,Album


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id', 'username')

class AlbumSerializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    imgurl = serializers.CharField()
    imglen = serializers.CharField()
    motif = serializers.CharField()
    time = serializers.DateTimeField(required=False)
    publisher = UserSerializers(read_only=True)
