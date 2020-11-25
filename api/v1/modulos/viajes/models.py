from django.db import models
from api.v1.modulos.choferes.models import Choferes
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


      def __str__(self):
         return '{}-{}'.format(self.origen, self.destino)
