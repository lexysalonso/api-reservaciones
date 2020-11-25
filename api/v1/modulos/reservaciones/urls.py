from django.urls import path , include
from rest_framework import routers
from .viewset import ReservacionesCreate

router = routers.DefaultRouter()
router.register('reservaciones' ,ReservacionesCreate,basename='reservaciones')

urlpatterns = [
    path('',include(router.urls))
]