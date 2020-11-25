from django.db import models
from api.v1.modulos.viajes.models import Viaje

class Reservacion(models.Model):
    fecha = models.CharField(max_length=10)
    viajes = models.ForeignKey(Viaje, related_name="reservaciones", on_delete=models.CASCADE)
    cis = models.CharField(max_length=100)
    asientos = models.IntegerField()

    def __str__(self):
        return '{}-{}'.format(self.fecha,self.viajes)