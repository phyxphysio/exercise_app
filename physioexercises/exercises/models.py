from django.db import models

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    image = models.ImageField(("Exercise Image"), upload_to='images', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name
