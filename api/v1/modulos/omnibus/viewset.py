from rest_framework.response import Response

from .serializer import OmnibusSerialzer
from .models import Omnibus
from api.v1.modulos.viajes.models import Viaje
from api.v1.modulos.viajes.serializer import ViajeSerealizer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status

class OmnibusCreate(ModelViewSet):
        def get_queryset(self):
           queryset = Omnibus.objects.all().order_by('capacidad')
           return queryset

        serializer_class = OmnibusSerialzer

        @action(methods=['patch'],detail=True,url_path='taller',url_name='taller')
        def taller(self,requests, pk=None):
            omnnibus = self.get_object()
            omnnibus.disponible = False
            omnnibus.save()
            return Response({'satatus':'Omnibus para taller'},status=status.HTTP_200_OK)

        @action(methods=['patch'],detail=True,url_path='disponible', url_name='disponible')
        def Disponible(self,request,pk=None):
              omnibus = self.get_object()
              omnibus.disponible = True
              omnibus.save()
              return Response({'satatus':'Omnibus ya disponible'},status=status.HTTP_200_OK)

        @action(methods=['get'],detail=True,url_name='viajes',url_path='viajes')
        def OmnibusViajes(self,request,pk=None):
            viajes = Viaje.objects.filter(omnibus_id=self.kwargs["pk"])
            print('ver viajes',viajes)
            serializer_context = {
                'request': request,
            }
            serializer = ViajeSerealizer(viajes, context=serializer_context, many=True,read_only=True)
            return Response(serializer.data, status=status.HTTP_200_OK)






