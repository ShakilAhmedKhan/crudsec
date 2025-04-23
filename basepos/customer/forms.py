from django import forms
from .models import Customer, Medicine


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'




class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'