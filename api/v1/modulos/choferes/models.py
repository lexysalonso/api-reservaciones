from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class Choferes(models.Model):
    nombre = models.CharField(max_length=255)
    ci = models.CharField(max_length=11, unique=True)
    create_by = models.ForeignKey(User, related_name='chofere', verbose_name='create of user', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='choferes', blank=True, db_table='v1_chofer_members')

    def __str__(self):
        return self.nombre

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
        return request.user.has_perm('v1.add_choferes')

    @staticmethod
    def has_update_permission(request):
        return request.user.has_perm('v1.change_choferes')

    @staticmethod
    def has_destroy_permission(request):
        return request.user.has_perm('v1.delete_choferes')

    @staticmethod
    def has_list_permission(request):
        return request.user.has_perm('v1.view_choferes')

    def has_object_update_permission(self, request):
        return self.has_generic_permission(request, 'change_choferes')

    def has_object_destroy_permission(self, request):
        return self.has_generic_permission(request, 'delete_choferes')

    def has_generic_permission(self, request, permision_codename):
        if request.user.is_superuser or request.user == self.create_by:
            return True
        member = Choferes.is_member(self, request.user)
        if member:
            return self.user_members_has_permission(request, permision_codename)
        return False

    def is_member(self, username):
        chofer = get_object_or_404(Choferes, pk=self.pk)
        objs = chofer.members.filter(username=username)
        if objs:
            return True
        return False

    def user_members_has_permission(self, request, permision_codename):
        return request.user.has_perm('v1.{}'.format(permision_codename))