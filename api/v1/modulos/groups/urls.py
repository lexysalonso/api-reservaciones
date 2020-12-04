from django.urls import include , path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .viewset import RegisterGroups

route = routers.DefaultRouter()
route.register('groups',RegisterGroups , basename='groups')
urlpatterns = [
    path('',include(route.urls))
]









