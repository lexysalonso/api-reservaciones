from django.db import models

class Choferes(models.Model):
    nombre = models.CharField(max_length=255)
    ci = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nombre