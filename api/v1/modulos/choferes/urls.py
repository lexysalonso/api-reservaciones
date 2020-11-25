from django.urls import path, include
from rest_framework import routers
from .viewset import ChoferesCreate

router = routers.DefaultRouter()
router.register('choferes', ChoferesCreate, basename='choferes')

urlpatterns = [
    path('',include(router.urls))
]