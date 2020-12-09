from django.db import models
from api.v1.modulos.viajes.models import Viaje
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class Reservacion(models.Model):
    fecha = models.CharField(max_length=10)
    viajes = models.ForeignKey(Viaje, related_name="reservaciones", on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, related_name='reservacion', verbose_name='create of user', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='reservaciones_members', blank=True, db_table='v1_reservacion_members')
    cis = models.CharField(max_length=100)
    asientos = models.IntegerField()

    def __str__(self):
        return '{}-{}'.format(self.fecha,self.viajes)

    @staticmethod
    def has_write_permission(request):
        return True

    @staticmethod
    def has_read_permission(request):
        return True

    @staticmethod
    def has_write_object_permission(request):
        return True

    @staticmethod
    def has_read_object_permission(request):
        return True

    @staticmethod
    def has_create_permission(request):
        return request.user.has_perm('v1.add_reservacion')

    @staticmethod
    def has_update_permission(request):
        return request.user.has_perm('v1.change_reservacion')

    @staticmethod
    def has_destroy_permission(request):
        return request.user.has_perm('v1.delete_reservacion')

    @staticmethod
    def has_list_permission(request):
        return request.user.has_perm('v1.view_reservacion')


    def has_object_update_permission(self,request):
        return self.has_generic_permission(request,'change_reservacion')

    def has_object_destroy_permission(self,request):
        return self.has_generic_permission(request,'delete_reservacion')


    def has_generic_permission(self,request,permision_codename):
        if request.user.is_superuser or request.user == self.create_by:
            return True
        member = Reservacion.is_member(self,request.user)
        if member:
            return self.user_members_has_permission(request,permision_codename)
        return False

    def is_member(self,username):
       reservacion =  get_object_or_404(Reservacion,pk = self.pk)
       objs = reservacion.members.filter(username=username)
       if objs:
           return True
       return False

    def user_members_has_permission(self,request,permision_codename):
         return request.user.has_perm('v1.{}'.format(permision_codename))



























































































































































































































