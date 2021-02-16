from django.db import models

# Create your models here.
class Clients(models.Model):
    id = models.IntegerField(primary_key=True)
    document = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Bills(models.Model):
    id = models.IntegerField(primary_key=True)
    cliets_id = models.IntegerField()
    company_name = models.CharField(max_length=100)
    nit = models.CharField(max_length=50)
    code = models.CharField(max_length=100)

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    nit = models.CharField(max_length=50)
    attribute = models.CharField(max_length=100)
