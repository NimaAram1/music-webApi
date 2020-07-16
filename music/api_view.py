from rest_framework import viewsets
from .models import Music
from .serializers import MusicSerializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser , AllowAny

class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializers
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]    
        return [permission() for permission in permission_classes]    

