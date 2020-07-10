from django.urls import path
from . import views
app_name = 'Music'
urlpatterns = [
    path('capture',views.capture,name='capture'),
    path('sign',views.sign,name='sign'),
    path('sign/<int:id>',views.signid,name='signid'),
]
