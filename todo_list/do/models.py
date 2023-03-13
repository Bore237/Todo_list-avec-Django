from django.db import models

# Create your models here.

class Task(models.Model):
    taches = models.CharField(max_length=150)
    title = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.taches
    
