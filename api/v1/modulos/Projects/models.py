from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User,Group,Permission

class Projects(models.Model):
     nombre = models.CharField(max_length=100)
     hora = models.DateTimeField(auto_now=True)
     create_by = models.ForeignKey(User, related_name='project',verbose_name='create of user', on_delete=models.CASCADE)
     members = models.ManyToManyField(User,related_name='projects',blank=True,db_table='v1_project_members')
     groups = models.ManyToManyField(Group,blank=True,db_table='v1_project_groups')
     permission = models.ManyToManyField(Permission,blank=True,db_table='v1_project_permision')

     def __str__(self):
          return self.nombre

     @staticmethod
     def has_read_permission(request):
          return True

     @staticmethod
     def has_write_permission(request):
          return True

     @staticmethod
     def has_object_write_permission(request):
         return True

     @staticmethod
     def has_object_read_permission(request):
         return True
     @staticmethod
     def has_create_permission(request):
          print('ver user ', request.user)
          return request.user.has_perm('v1.add_projects')

     @staticmethod
     def has_destroy_permission(request):
          print('ver user ', request.user)
          return request.user.has_perm('v1.delete_projects')

     def has_object_update_permission(self, request):

          return self.has_generic_permission(request)

     def has_generic_permission(self, request):
          print("veer member", request.user , self.create_by)
          if request.user.is_superuser or request.user == self.create_by:

              return True
          member = Projects.is_member(request.user, self)
          if member:
                return request.user.has_perm('v1.change_projects')
          return False

     def is_member(username,self):
           obj = get_object_or_404(Projects,pk=self.id)
           member = obj.members.filter(username=username)

           if member:
               return True
           return False







               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               







































































































































