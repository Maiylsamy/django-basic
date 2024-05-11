from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    name = models.ForeignKey(Author,on_delete=models.CASCADE)
    publish_date = models.DateField()

    def __str__(self):
        return self.title