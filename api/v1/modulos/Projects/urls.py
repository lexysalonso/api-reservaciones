from django.urls import include , path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .viewset import Projectsall

route = routers.DefaultRouter()
route.register('projects',Projectsall, basename='projects')

urlpatterns = [
    path('',include(route.urls))
]