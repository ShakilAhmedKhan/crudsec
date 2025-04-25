from django.urls import path, include
from .views import (
    CustomerListView, CustomerCreateView, CustomerUpdateView,
    CustomerDetailView, CustomerDeleteView, CustomerViewSet, SellMedicineView, MedicineListView, MedicineCreateView, SaleListView
)
from rest_framework.routers import DefaultRouter

# API
router = DefaultRouter()
router.register('customers', CustomerViewSet)

# HTML
urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    path('add/', CustomerCreateView.as_view(), name='customer-add'),
    path('<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer-edit'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
    path('api/', include(router.urls)),  # REST API path

    path('sell/', SellMedicineView.as_view(), name='sell-medicine'),
    #Medicine URL Group
    path('medicine/', MedicineListView.as_view(), name='medicine-list'),
    path('medicine/add', MedicineCreateView.as_view(), name='medicine-add'),
    path('medicine/<int:pk>/edit', SellMedicineView.as_view(), name='medicine-edit'),
    path('medicine/<int:pk>/', SellMedicineView.as_view(), name='medicine-detail'),
    path('medicine/<int:pk>/delete', SellMedicineView.as_view(), name='medicine-delete'),


    #Invoices
    path('invoices/', SaleListView.as_view(), name='invoices-list'),
]