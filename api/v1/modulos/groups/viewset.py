from rest_framework import generics,permissions,mixins,viewsets
from rest_framework.response import Response
from .serializer import GroupsrSerealizer, UserSerealizer
from django.contrib.auth.models import Group

class RegisterGroups(viewsets.ModelViewSet):
      queryset = Group.objects.all()
      serializer_class = GroupsrSerealizer


















