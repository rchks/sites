from django.db import models
from geoposition.fields import GeopositionField
# Create your models here.

class Section(models.Model):
    Tag = models.CharField(max_length=255, default="", null=False)
    Title = models.CharField(max_length=255, null=False)
    Definition = models.TextField(max_length=100000, null=False)
    Picture = models.ImageField(null=True, blank=True)



class Article(models.Model):
    Tag = models.ManyToManyField(Section)
    Title = models.CharField(max_length=255, null=False)
    Descrip = models.TextField(max_length=100000, null=False)
    Location = models.CharField(max_length=255)
    Transport = models.CharField(max_length=255)
    Picture = models.ImageField(upload_to="post/", null=True, blank=True)

