# HTML Views (Template-Based)
from pyclbr import Class

from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Customer, Medicine
from .forms import CustomerForm, MedicineForm
from django.db.models import Q
from django.core.paginator import Paginator

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 10 # Shows 10 per page

    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = super().get_queryset()
        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(phone__icontains=query) |
                Q(email__icontains=query)
            )

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/customer_form.html'
    success_url = reverse_lazy('customer-list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/customer_form.html'
    success_url = reverse_lazy('customer-list')

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer/customer_confirm_delete.html'
    success_url = reverse_lazy('customer-list')



class SellMedicineView(View):
    #model = Customer
    template_name = 'customer/sell_medicine.html'
    def get(self, request, *args, **kwargs):
        #sale_form = SaleForm()
        #formset = SaleItemFormSet()
        customers = Customer.objects.all()
        medicines = Medicine.objects.all()

        return render(request, self.template_name, {
          #  'sale_form': sale_form,
           # 'formset': formset,
            'customers': customers,
            'medicines': medicines,
        })


#Medicine Views

class MedicineListView(ListView):
    model = Medicine
    template_name = 'medicine/medicine_list.html'

class MedicineCreateView(CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'medicine/medicine_form.html'
    success_url = reverse_lazy('medicine-list')
class MedicineUpdateView(UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'medicine/medicine_form.html'
    success_url = reverse_lazy('medicine-list')

class MedicineDetailView(DetailView):
    model = Medicine
    template_name = 'medicine/medicine_detail.html'

class MedicineDeleteView(DeleteView):
    model = Medicine
    template_name = 'medicine/medicine_confirm_delete.html'
    success_url = reverse_lazy('medicine-list')







# API Views
from rest_framework import viewsets
from .serializers import CustomerSerializer , MedicineSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer