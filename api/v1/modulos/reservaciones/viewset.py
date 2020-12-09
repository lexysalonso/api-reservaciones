from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from dry_rest_permissions.generics import DRYGlobalPermissions,DRYObjectPermissions
from rest_framework.viewsets import ModelViewSet
from .models import Reservacion
from rest_framework.permissions import IsAuthenticated
from .serializer import  ReservacionSerialaizer
import os
class ReservacionesCreate(ModelViewSet):
       queryset = Reservacion.objects.all()
       serializer_class = ReservacionSerialaizer
       permission_classes = (IsAuthenticated,DRYObjectPermissions,DRYGlobalPermissions)

