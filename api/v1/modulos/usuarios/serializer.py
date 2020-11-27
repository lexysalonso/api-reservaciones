from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from django.contrib.auth import authenticate

class RegisterUserSerealizer(serializers.ModelSerializer):
          class Meta:
               model = User
               fields = ('username','password','email','first_name','last_name')
               extra_kwargs = {
                   'password':{
                       'write_only':True
                   },
               }

          def create(self, validate_data):
                   user = User.objects.create_user(validate_data['username'],
                                                   password=validate_data['password'],
                                                   first_name=validate_data['first_name'],
                                                   last_name=validate_data['last_name']

                                                   )
                   user.set_password(validate_data['password'])
                   user.save()
                   return user

class UserSerealizer(serializers.ModelSerializer):
      class Meta:
          model = User
          fields = '__all__'
