from rest_framework import routers
from music.api_view import MusicViewSet


router = routers.DefaultRouter()
router.register('api',MusicViewSet,basename='music')