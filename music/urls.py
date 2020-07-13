from django.urls import path
from . import views
from .api_url import router


app_name = 'Music'
urlpatterns = router.urls
