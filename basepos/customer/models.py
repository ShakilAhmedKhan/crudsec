from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    point = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField(max_length=100, default=10)
    stock = models.IntegerField()
    shelf = models.CharField(max_length=10)
    purpose = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name


class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Invoice #{self.id} - {self.customer.name}"




