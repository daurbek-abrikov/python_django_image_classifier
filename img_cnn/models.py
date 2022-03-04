from django.db import models
from sqlalchemy import true

# Create your models here.
class Test(models.Model): 
    name = models.CharField(max_length=100, primary_key=true)
    image = models.ImageField(default="")

    def __str__(self):
        return self.name
