from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField(null=True)
    message=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    food = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return self.phone  
