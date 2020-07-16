from rest_framework import serializers
from .models import Music
class MusicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Music
        exclude = ['id']


    def validate_name(self,value):
        if value == 'admin':
            raise serializers.ValidationError('name can not be admin')
        return value    
