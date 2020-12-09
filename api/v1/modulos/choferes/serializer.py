from rest_framework import serializers
from .models import Choferes
from api.v1.modulos.usuarios.serializer import UserSerealizer

class ChoferesSerializer(serializers.ModelSerializer):
       url = serializers.HyperlinkedIdentityField(view_name="choferes:choferes-detail")
       #create_by = UserSerealizer()
       class Meta:
              model = Choferes
              fields = ('url','nombre', 'ci','create_by','members')