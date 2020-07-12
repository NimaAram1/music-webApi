from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from .models import Music
from .serializers import MusicSerializers
from rest_framework import status
from rest_framework.permissions import IsAdminUser , AllowAny
# @api_view()
@api_view(['GET','POST'])
def capture(request):
    if request.method == 'POST':
        name = request.data['name']
        return Response({'body':f"{name} Profile"})
    else:
        return Response({'error':"1000"})

@api_view()
@permission_classes([AllowAny])
def sign(request):
    mus = Music.objects.all()
    ser_data =  MusicSerializers(mus,many=True)
    return Response(ser_data.data,status=status.HTTP_200_OK)


@api_view()
@permission_classes([AllowAny])
def signid(request,id):
    try:
        music = Music.objects.get(pk=id)
    except Music.DoesNotExist:
        return Response({'error':'404'},status=status.HTTP_404_NOT_FOUND)
    ser_data = MusicSerializers(music)
    return Response(ser_data.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def relase(request):
    info = MusicSerializers(request.FILES,data=request.data)
    if info.is_valid():
        Music(name=info.validated_data['name'],cover=info.validated_data['cover'],
        song=info.validated_data['song'],artist=info.validated_data['artist']).save()
        music_sv = info.validated_data['name']
        return Response({'message':'ok','song':f'{music_sv}'},status=status.HTTP_201_CREATED)

    else:
        return Response(info.errors,status=status.HTTP_400_BAD_REQUEST)                     
