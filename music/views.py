from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from .models import Music
from .serializers import MusicSerializers
from rest_framework import status
from rest_framework.permissions import IsAdminUser , AllowAny


