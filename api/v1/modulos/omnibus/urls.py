from django.urls import include , path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .viewset import OmnibusCreate

route = routers.DefaultRouter()
route.register('omnibus',OmnibusCreate, basename='omnibus')

urlpatterns = [
    path('',include(route.urls))
]
