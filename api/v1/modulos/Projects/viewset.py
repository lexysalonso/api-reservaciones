from dry_rest_permissions.generics import DRYGlobalPermissions, DRYObjectPermissions
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Projects
from .serializer import ProjectsSerializer
from rest_framework.permissions import IsAuthenticated

class Projectsall(viewsets.ModelViewSet):
     queryset = Projects.objects.all()
     serializer_class = ProjectsSerializer
     permission_classes = (DRYGlobalPermissions,DRYObjectPermissions)

     def perform_create(self, serializer):
          create_by = self.request.user
          serializer.save(create_by=create_by)