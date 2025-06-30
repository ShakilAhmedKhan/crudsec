from django import forms
from .models import Customer, Medicine, Sale


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'dd/mm/yyyy',
                    'class': 'form-control'
                },
                format='%d/%m/%Y'
            ),
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].input_formats = ['%d/%m/%Y']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

class  SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer']