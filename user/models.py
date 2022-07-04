from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=20)

class UserAdmin(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    is_admin = models.BooleanField()
