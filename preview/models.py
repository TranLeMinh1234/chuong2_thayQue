from email.mime import image
from pydoc import describe
from django.db import models

# Create your models here.
class Book(models.Model):
  name = models.CharField(max_length=224, null=False, blank=False)
  description = models.TextField(max_length=254, null=False, blank=False)
  price = models.FloatField(null=False)
  image = models.ImageField()

  def __unicode__(self):
    return self.content