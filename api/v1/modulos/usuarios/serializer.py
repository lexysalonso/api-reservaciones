from django.contrib.auth.models import User,Permission
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from django.contrib.auth import authenticate

class RegisterUserSerealizer(serializers.ModelSerializer):

          class Meta:
               model = User
               fields = ('username','password','email','first_name','last_name','user_permissions','groups')
               extra_kwargs = {
                   'password':{
                       'write_only':True
                   },
               }

          def create(self, validate_data):
                  permissions = validate_data.get('user_permissions')
                  groups = validate_data.get('groups')
                  perm = []
                  gps = []
                  for item in permissions:
                      perm.append(item)
                  for item in groups:
                      gps.append(item)
                  user = User.objects.create_user(validate_data['username'],
                                                   password=validate_data['password'],
                                                   first_name=validate_data['first_name'],
                                                   last_name=validate_data['last_name']

                                                   )
                  user.set_password(validate_data['password'])
                  user.user_permissions.set(permissions)
                  user.groups.set(gps)
                  user.save()
                  return user

class UserSerealizer(serializers.ModelSerializer):
      class Meta:
          model = User
          fields = '__all__'
