from rest_framework import serializers
from .models import Choferes

class ChoferesSerializer(serializers.HyperlinkedModelSerializer):
       url = serializers.HyperlinkedIdentityField(view_name="choferes:choferes-detail")
       class Meta:
              model = Choferes
              fields = ('nombre', 'ci','url')