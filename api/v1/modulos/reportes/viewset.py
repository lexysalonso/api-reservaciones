from rest_framework.decorators import action

from api.v1.modulos.omnibus.models import Omnibus
from api.v1.modulos.viajes.models import Viaje
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import filters
from rest_framework.response import Response
from api.v1.modulos.omnibus.serializer import OmnibusSerialzer
from api.v1.modulos.viajes.serializer import ViajeSerealizer
from api.v1.modulos.viajes.models import Viaje
from rest_framework.permissions import IsAuthenticated


class OmnibusTaller(viewsets.GenericViewSet):

       permission_classes = (IsAuthenticated ,)


       @action(methods=['get'],detail=False,url_path='omnibustaller', url_name='omnibustaller')
       def listOmnibus(self,request):
          queryset1 = Omnibus.objects.filter(disponible=False)
          serialzer = OmnibusSerialzer(queryset1,context=self.get_serializer_context(),many=True)
          return Response(serialzer.data, status=status.HTTP_201_CREATED )

       @action(methods=['get'],detail=False,url_name='omnibus-mas-viajes',url_path='omnibus-mas-viajes')
       def OmnibusMasViajes(self,request):
           omnibus = {}
           mas_viajes = []
           queryset = Viaje.objects.all()
           for item in queryset:
                   numero = item.omnibus.numero
                   if numero not in omnibus:

                       omnibus[numero]= {}
                       omnibus[numero]['numero'] = numero
                       omnibus[numero]['chapa'] = item.omnibus.chapa
                       omnibus[numero]['cantidad'] = 1

                   else:
                        omnibus[numero]['cantidad'] +=  1

           for item in omnibus:
                mas_viajes.append(omnibus[item])
                for item in mas_viajes:
                    print('ver chapa',item['chapa'])
           return Response(mas_viajes,status=status.HTTP_200_OK)





