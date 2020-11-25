from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Choferes
from .serializer import ChoferesSerializer


class ChoferesCreate(ModelViewSet):
      queryset = Choferes.objects.all()
      serializer_class = ChoferesSerializer
