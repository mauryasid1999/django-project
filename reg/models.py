from django.db import models


# Create your models here.
class fbpage(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    mobile=models.IntegerField()
    password=models.IntegerField()
    dateof_birth=models.DateField()
    gender=models.CharField(max_length=5)