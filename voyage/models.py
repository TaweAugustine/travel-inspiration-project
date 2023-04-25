from django.db import models

from django.contrib.auth.models import User


class TravelInspiration(models.Model):
    budget = models.DecimalField(max_digits=20,decimal_places=0,null=False,verbose_name="Budget du voyage")
    travel_date_start = models.DateField(verbose_name="Date de Demarrage du voyage")
    travel_date_end = models.DateField(verbose_name="Date de Retour du voyage")
    prefered_activitties = models.CharField(verbose_name="prefered_activitties",max_length=500)


class Favorites(models.Model):
    users = models.ManyToManyField(to=User,related_name="favorites")
    travel_inspiration = models.ForeignKey(to=TravelInspiration,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

