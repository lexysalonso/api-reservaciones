from rest_framework.viewsets import ModelViewSet
from .models import Reservacion
from rest_framework.permissions import IsAuthenticated
from .serializer import  ReservacionSerialaizer

class ReservacionesCreate(ModelViewSet):
       queryset = Reservacion.objects.all()
       serializer_class = ReservacionSerialaizer
       permission_classes = (IsAuthenticated,)