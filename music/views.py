from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Music
from .serializers import MusicSerializers
# @api_view()
@api_view(['GET','POST'])
def capture(request):
    if request.method == 'POST':
        name = request.data['name']
        return Response({'body':f"{name} Profile"})
    else:
        return Response({'error':"1000"})

@api_view()
def sign(request):
    mus = Music.objects.all()
    ser_data =  MusicSerializers(mus,many=True)
    return Response(ser_data.data)


@api_view()
def signid(request,id):
    try:
        music = Music.objects.get(pk=id)
    except Music.DoesNotExist:
        return Response({'error':'this music is not availabele'})
    ser_data = MusicSerializers(music)
    return Response(ser_data.data)              
