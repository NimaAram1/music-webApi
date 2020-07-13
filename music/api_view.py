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

    # def list(self,request):
    #     queryset = Music.objects.all()
    #     serializer = MusicSerializers(queryset,many=True)
    #     return Response(serializer.data)

    # def retrieve(self,request,pk=None):
    #     queryset = Music.objects.all()
    #     music = get_object_or_404(queryset,pk=pk)

    # def create(self,request):
    #     serializer = MusicSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message':'SUCCESS'})
    #     else:
    #         return Response(serializer.errors)        

