from django.contrib import admin
from .models import Sale, SaleItem, Customer, Medicine

admin.site.register(Customer)
admin.site.register(Medicine)
admin.site.register(Sale)
admin.site.register(SaleItem)
