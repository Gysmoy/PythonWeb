from django.urls import path
from manage_it_service.APIs import supplierAPI as views
urlpatterns = [
    path('setSupplier/', views.setSupplier.as_view()),
    path('getSuppliers/', views.getSuppliers.as_view()),
    path('getActivesSuppliers/', views.getActivesSuppliers.as_view()),
    path('getInactiveSubscription/', views.getInactivesSuppliers.as_view()),
    path('updateSupplier/', views.updateSupplier.as_view()),
    path('deleteSupplier/', views.deleteSupplier.as_view()),
    path('restoreSupplier/', views.restoreSupplier.as_view()),
]