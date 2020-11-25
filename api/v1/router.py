from django.urls import include, path
from django.urls import path, include
from rest_framework import routers
from rest_framework.response import Response
from rest_framework.views import APIView


class DocsView(APIView):
    """
    RESTFul Documentation of my app
    """
    def get(self, request, *args, **kwargs):
        apidocs = {'omnibus': request.build_absolute_uri('omnibus/'),
                   'choferes': request.build_absolute_uri('choferes/'),
                   'viajes': request.build_absolute_uri('viajes/'),
                   'api4title': request.build_absolute_uri('api4endpoint/'),
                   }
        return Response(apidocs)

urlpatterns = [
    path('',DocsView.as_view()),
    path('', include(('api.v1.modulos.omnibus.urls', 'omnibus'))),
    path('', include(('api.v1.modulos.choferes.urls', 'choferes'))),
    path('', include(('api.v1.modulos.viajes.urls', 'viajes'))),
]