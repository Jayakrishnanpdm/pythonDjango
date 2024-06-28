from django.db import models

# Create your models here.
class Censor_info(models.Model):
    rating=models.CharField(max_length=5)
    certified_by=models.CharField(max_length=20)

class Actors(models.Model):
    name=models.CharField(max_length=20)

class Directors(models.Model):
    name = models.CharField(max_length=20)   
   
class movie_info(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField(null=True)
    summary = models.TextField()
    poster=models.ImageField(upload_to='images/',null=True, blank=True)
    censor_details=models.OneToOneField(Censor_info,null=True,on_delete=models.SET_NULL,related_name='movies')
    directed_by=models.ForeignKey(Directors,null=True,on_delete=models.CASCADE,related_name='directed_movie')
    actors=models.ManyToManyField(Actors,related_name='actor')
    def __str__(self):
        return f"{self.title} ({self.pk})"
     
