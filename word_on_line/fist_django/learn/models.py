from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=2)
    where = models.CharField(max_length=30)
    job = models.CharField(max_length=50)
    hobby = models.CharField(max_length=100)

    def __str__(self):
        return self.name


