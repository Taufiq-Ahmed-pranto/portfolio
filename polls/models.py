from django.contrib.messages.api import info
from django.db import models

# Create your models here.

class Project(models.Model):
    projectId= models.CharField(max_length=2000)
    name= models.CharField(max_length=2000)
    img= models.ImageField(upload_to = 'pics')
    desc= models.TextField()
    link= models.CharField(max_length=2000)
    private= models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
