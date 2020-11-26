from django.urls import path, include
from rest_framework import routers
from .viewset import OmnibusTaller


route = routers.DefaultRouter()
route.register('reportes',OmnibusTaller,basename='reportes')

urlpatterns = [
    path('',include(route.urls))
]