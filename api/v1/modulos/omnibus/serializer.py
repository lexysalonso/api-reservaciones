from rest_framework.serializers import ModelSerializer
from  rest_framework import serializers
from .models import Omnibus
from  api.v1.modulos.viajes.serializer import ViajeSerealizer

class OmnibusSerialzer(serializers.ModelSerializer):
          #omnibus = ViajeSerealizer(many=True,read_only=True, required=False)
          url = serializers.HyperlinkedIdentityField(view_name="omnibus:omnibus-detail")
          viajes = serializers.HyperlinkedIdentityField(view_name="omnibus:omnibus-viajes")
          class Meta:
               model = Omnibus
               fields = ('numero', 'chapa', 'disponible', 'capacidad','url','viajes')
