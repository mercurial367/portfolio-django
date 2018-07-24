from django.db import models

class Projects(models.Model):
    images = models.ImageField(upload_to='images/')
    link = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
