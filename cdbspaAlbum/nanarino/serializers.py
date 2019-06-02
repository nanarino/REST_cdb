from rest_framework import serializers


class UserSerializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField()


class AlbumSerializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    imgurl = serializers.CharField()
    imglen = serializers.CharField()
    motif = serializers.CharField()
    time = serializers.DateTimeField(required=False)
    publisher = UserSerializers(read_only=True)
    publisher_id = UserSerializers(write_only=True)
