from django.db import models

# Create your models here.

class Dog(models.Model):
    name =models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

class AccountUser(models.Model):
    username = models.CharField(max_length=100)
    realName =models.CharField(max_length=100)
    accountNumber = models.IntegerField(max_length=15)
    balance = models.DecimalField(max_digits=10, decimal_places=3)
