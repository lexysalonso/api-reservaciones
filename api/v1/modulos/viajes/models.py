from django.db import models
from api.v1.modulos.choferes.models import Choferes
from django.contrib.auth.models import User
from api.v1.modulos.omnibus.models import Omnibus


class Destino(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=50)


    def __str__(self):
       return self.nombre


class Viaje(models.Model):
      hora = models.CharField(max_length=5)
      omnibus = models.ForeignKey(Omnibus, related_name='omnibus', on_delete=models.CASCADE)
      chofer1 = models.ForeignKey(Choferes, related_name='chofer1', on_delete=models.CASCADE)
      chofer2 = models.ForeignKey(Choferes, related_name='chofer2', on_delete=models.CASCADE)
      origen = models.ForeignKey(Destino, related_name='origen', on_delete=models.CASCADE)
      destino = models.ForeignKey(Destino, related_name='destino', on_delete=models.CASCADE)
      create_by = models.ForeignKey(User, related_name='users', verbose_name='create of user',on_delete=models.CASCADE)

      def __str__(self):
         return '{}-{}'.format(self.origen, self.destino)

      @staticmethod
      def has_read_permission(request):
          return True

      @staticmethod
      def has_write_permission(request):
          return True

      @staticmethod
      def has_object_read_permission(request):
          return True

      @staticmethod
      def has_object_write_permission(request):
          return True

      def has_create_permission(request):
          return request.user.has_perm('v1.add_viaje')

      def has_update_permission(request):
          return request.user.has_perm('v1.change_viaje')

      def has_destroy_permission(request):
          return request.user.has_perm('v1.delete_viaje')

      def has_view_permission(request):
          return request.user.has_perm('v1.view_viaje')

      def has_object_update_permission(self, request, ):
          return self.has_generic_permission(request, 'change_viaje')

      def has_object_destroy_permission(self, request, ):
          return self.has_generic_permission(request, 'delete_viaje')

      def has_generic_permission(self, request, codename_permission):
          if request.user.is_superuser or request.user == self.create_by:
              return request.user.has_perm('v1.{}'.format(codename_permission))
          return False
