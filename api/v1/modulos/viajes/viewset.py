from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from .utils import ProductFilter
from rest_framework.views import APIView
from rest_framework import status
from .models import Viaje , Destino
from api.v1.modulos.omnibus.models import Omnibus
from django.shortcuts import get_object_or_404
from .serializer import ViajeSerealizer, DestinoSerializer

class DestinoCreate(ListCreateAPIView):
      queryset = Destino.objects.all()
      serializer_class = DestinoSerializer


class ViajeCreate(ModelViewSet):
      queryset = Viaje.objects.all()
      serializer_class = ViajeSerealizer
      filter_class = ProductFilter







