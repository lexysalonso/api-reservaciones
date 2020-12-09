from rest_framework  import serializers
from .models import Reservacion

class ReservacionSerialaizer(serializers.ModelSerializer):
       url = serializers.HyperlinkedIdentityField(view_name="reservaciones:reservaciones-detail")
       class Meta:
           model = Reservacion
           fields = ('url','fecha','viajes','cis','asientos','create_by','members')
