from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from django.contrib.auth import authenticate

class GroupsrSerealizer(serializers.ModelSerializer):
          class Meta:
               model = Group
               fields = ('name','permissions')


          def create(self, validate_data):
              items = validate_data.get('permissions')

              permissions = []
              for item in items:
                  permissions.append(item)
                  print('ver', permissions)
              gropus = Group.objects.create(name=validate_data['name'],
                                            )

              gropus.permissions.set(permissions)

              gropus.save()
              return gropus

class UserSerealizer(serializers.ModelSerializer):
      class Meta:
          model = User
          fields = '__all__'
