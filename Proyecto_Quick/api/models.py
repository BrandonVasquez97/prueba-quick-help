from tkinter import CASCADE
from django.db import models

# Create your models here.
class Clients(models.Model):
    document = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

class Users(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    active = models.IntegerField()

class Tokens(models.Model):
    token = models.CharField(max_length=300)
    active = models.IntegerField()
    expiry_date = models.DateTimeField(max_length=20)
    user_id = models.ForeignKey("Users", on_delete=models.CASCADE)

class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    Attribute_4 = models.CharField(max_length=50)

class Bills(models.Model):
    client_id = models.ForeignKey("Clients", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    nit = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

class Bills_Products(models.Model):
    bill_id = models.ForeignKey("Bills", on_delete=models.CASCADE)
    product_id = models.ForeignKey("Products", on_delete=models.CASCADE)
