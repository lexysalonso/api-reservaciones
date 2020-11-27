from rest_framework import generics,permissions,mixins
from rest_framework.response import Response
from .serializer import RegisterUserSerealizer, UserSerealizer
from django.contrib.auth.models import User

class RegisterUser(generics.GenericAPIView):
      serializer_class = RegisterUserSerealizer

      def post(self,request,*args,**kwargs):
          serilizer =  self.get_serializer(data=request.data)
          serilizer.is_valid(raise_exception=True)
          user = serilizer.save()
          return Response({"user": UserSerealizer(user,context=self.get_serializer_context()).data,
                            "message":"User create Successfully"

                           })
