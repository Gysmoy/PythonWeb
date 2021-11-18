from django.urls import path
from manage_it_service.APIs import personAPI as views

urlpatterns = [
    path('setP_natural/', views.setP_natural.as_view()),
    path('getP_naturales/', views.getP_naturales.as_view()),
    path('getActiveP_naturales/', views.getActiveP_naturales.as_view()),
    path('getInactiveP_naturales/', views.getInactiveP_naturales.as_view()),
    path('searchP_natural/', views.searchP_natural.as_view()),
    path('updateP_natural/', views.updateP_natural.as_view()),
    path('deleteP_natural/', views.deleteP_natural.as_view()),
    path('restoreP_natural/', views.restoreP_natural.as_view()),
    ]
