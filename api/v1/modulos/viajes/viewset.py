from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView

from api.v1.modulos.reservaciones.models import Reservacion
from api.v1.modulos.reservaciones.serializer import ReservacionSerialaizer
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

      @action(methods=['get'], detail=True, url_name='reservaciones', url_path='reservaciones')
      def ViajesReservaciones(self, request, pk=None):
            reservaciones = Reservacion.objects.filter(viajes_id=self.kwargs["pk"])
            print('ver viajes', reservaciones)
            serializer_context = {
                  'request': request,
            }
            serializer = ReservacionSerialaizer(reservaciones, context=serializer_context,many=True, read_only=True)
            return Response(serializer.data, status=status.HTTP_200_OK)







