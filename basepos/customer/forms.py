from django import forms
from .models import Customer, Medicine, Sale


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        #fields = '__all__'
        fields = ['name', 'email', 'phone', 'address','date_of_birth']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

class  SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer']