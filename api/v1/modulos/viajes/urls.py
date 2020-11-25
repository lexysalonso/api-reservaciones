from django.urls import path, include
from .models import Viaje
from .viewset import ViajeCreate , DestinoCreate
from rest_framework import routers

router = routers.DefaultRouter()
router.register('viajes',ViajeCreate, basename='viajes' )

urlpatterns = [
    path('', include(router.urls)),
    path('viajes/destino',DestinoCreate.as_view(), name='destino'),

]
