from rest_framework.viewsets import ModelViewSet
from .models import Reservacion
from .serializer import  ReservacionSerialaizer

class ReservacionesCreate(ModelViewSet):
       queryset = Reservacion.objects.all()
       serializer_class = ReservacionSerialaizer