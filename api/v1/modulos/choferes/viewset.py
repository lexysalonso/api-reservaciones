from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Choferes
from .serializer import ChoferesSerializer
from rest_framework.permissions import IsAuthenticated

class ChoferesCreate(ModelViewSet):
      queryset = Choferes.objects.all()
      serializer_class = ChoferesSerializer
      permission_classes = (IsAuthenticated,)
