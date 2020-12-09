from django.db import models
from django.contrib.auth.models import User

class Omnibus(models.Model):
    numero = models.IntegerField()
    chapa = models.CharField(max_length=7)
    disponible = models.BooleanField(default=True)
    capacidad = models.IntegerField()
    create_by = models.ForeignKey(User, related_name='omnibu', verbose_name='create of user', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.numero)

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

    @staticmethod
    def has_omnibusviajes_permission(request):
        return request.user.has_perm('v1.view_omnibus')

    def has_OmnibusMasViajes_permission(request):
        return request.user.has_perm('v1.view_omnibus')

    def has_create_permission(request):
        return request.user.has_perm('v1.add_omnibus')
    
    def has_update_permission(request):
        return request.user.has_perm('v1.change_omnibus')
    
    def has_destroy_permission(request):
        return request.user.has_perm('v1.delete_omnibus')
    
    def has_list_permission(request):
        return request.user.has_perm('v1.view_omnibus')
    
    def has_object_update_permission(self,request,):
        return self.has_generic_permission(request,'change_omnibus')

    def has_object_destroy_permission(self,request,):
        return self.has_generic_permission(request,'delete_omnibus')

    def has_generic_permission(self,request,codename_permission):
        if request.user.is_superuser or request.user == self.create_by:
              return request.user.has_perm('v1.{}'.format(codename_permission))
        return False

