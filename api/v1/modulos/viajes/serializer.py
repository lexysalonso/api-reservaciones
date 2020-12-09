from .models import Viaje , Destino
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.fields import empty
from api.v1.modulos.omnibus.models import Omnibus

class ViajeSerealizer(serializers.ModelSerializer):
        omnibus = serializers.PrimaryKeyRelatedField(queryset=Omnibus.objects.filter(disponible=True))
        reservaciones = serializers.HyperlinkedIdentityField(view_name="viajes:viajes-reservaciones")
        class Meta:
            model = Viaje
            fields = ['hora','omnibus','chofer1','chofer2','origen','destino','reservaciones','create_by']




class DestinoSerializer(ModelSerializer):
        class Meta:
            model = Destino
            fields = ('nombre', 'numero')