from django.db import models

class Omnibus(models.Model):
    numero = models.IntegerField()
    chapa = models.CharField(max_length=7)
    disponible = models.BooleanField(default=True)
    capacidad = models.IntegerField()

    def __str__(self):
        return str(self.numero)