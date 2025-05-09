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
    sale_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField(default=0)

    def __str__(self):
        return f"Invoice #{self.id} - {self.customer.name}"


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_at_sale = models.FloatField()

    def __str__(self):
        return f"{self.medicine.name} x {self.quantity}"




#ML model

class SuggestedMedicine(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    score = models.FloatField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('customer', 'medicine', 'created_at')
        ordering = ['-score']
