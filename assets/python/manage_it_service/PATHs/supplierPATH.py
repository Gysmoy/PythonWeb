from django.urls import path
from manage_it_service.APIs import supplierAPI as views
urlpatterns = [
    path('getSuppliers/', views.getSuppliers.as_view()),
    path('getActivesSuppliers/', views.getActivesSuppliers.as_view()),
    path('getInactivesSuppliers/', views.getInactivesSuppliers.as_view()),
    path('deleteSupplier/', views.deleteSupplier.as_view()),
    path('restoreSupplier/', views.restoreSupplier.as_view()),
]