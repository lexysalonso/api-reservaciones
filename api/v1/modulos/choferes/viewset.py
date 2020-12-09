from rest_framework import filters
from dry_rest_permissions.generics import DRYGlobalPermissions,DRYObjectPermissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Choferes
from .serializer import ChoferesSerializer
from rest_framework.permissions import IsAuthenticated




class ChoferesCreate(ModelViewSet):
      queryset = Choferes.objects.all()
      serializer_class = ChoferesSerializer
      permission_classes = (IsAuthenticated,DRYObjectPermissions,DRYGlobalPermissions)
      filter_backends = [filters.SearchFilter]
      search_fields = ['nombre']

      # def perform_create(self, serializer):
      #       create_by = self.request.user
      #       serializer.save(create_by=create_by)

