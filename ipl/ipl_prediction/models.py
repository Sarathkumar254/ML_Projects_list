from django.db import models

# Create your models here.
class IPL(models.Model):
	
 	bat_team_name = models.CharField(max_length=100)
 	bowl_team_name = models.CharField(max_length=100)
 	image = models.ImageField()