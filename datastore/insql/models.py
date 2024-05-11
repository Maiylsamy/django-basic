from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    place = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    score = models.IntegerField(null=True)




