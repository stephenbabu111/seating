from django.db import models


# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)

    def __str__(self):
        return self.name
