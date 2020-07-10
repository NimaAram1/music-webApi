from rest_framework import serializers

class MusicSerializers(serializers.Serializer):
    name = serializers.CharField()
    cover = serializers.ImageField()
    song = serializers.FileField()
    artist = serializers.CharField()
