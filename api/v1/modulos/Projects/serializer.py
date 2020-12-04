from rest_framework import serializers
from .models import Projects

class ProjectsSerializer(serializers.ModelSerializer):
      #permission = serializers.PrimaryKeyRelatedField(queryset= p.permission.filter(name=" Can change sesion"))
      class Meta:
           model = Projects
           fields = '__all__'