from tabnanny import verbose
from django.db import models

# Create your models here.
class Card(models.Model):
  id = models.AutoField(primary_key = True, verbose_name = 'ID')
  name = models.CharField(verbose_name = 'Nome', max_length = 20)
  cost = models.IntegerField(verbose_name = 'Custo')
  hp = models.IntegerField(verbose_name = 'Vida')
  atk = models.IntegerField(verbose_name = 'Ataque')
  lore = models.TextField(verbose_name = 'História')
  img = models.TextField(verbose_name = 'Arte')

  def __str__(self):
    return self.name