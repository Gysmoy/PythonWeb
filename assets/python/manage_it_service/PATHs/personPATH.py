from django.urls import path
from manage_it_service.APIs import personAPI as views

urlpatterns = [

    # Persona Natural

    path('setP_natural/', views.setP_natural.as_view()),
    path('getP_naturales/', views.getP_naturales.as_view()),
    path('getActiveP_naturales/', views.getActiveP_naturales.as_view()),
    path('getInactiveP_naturales/', views.getInactiveP_naturales.as_view()),
    path('searchP_natural/', views.searchP_natural.as_view()),
    path('updateP_natural/', views.updateP_natural.as_view()),
    path('deleteP_natural/', views.deleteP_natural.as_view()),
    path('restoreP_natural/', views.restoreP_natural.as_view()),

    # Persona Juridica

    path('setPJuridica/', views.setPJuridica.as_view()),
    path('getPJuridica/', views.getPJuridica.as_view()),
    path('getActivePJuridica/', views.getActivePJuridica.as_view()),
    path('getInactivePJuridica/', views.getInactivePJuridica.as_view()),
    path('searchPJuridica/', views.searchPJuridica.as_view()),
    path('updatePJuridica/', views.updatePJuridica.as_view()),
    path('deletePJuridica/', views.deletePJuridica.as_view()),
    path('restorePJuridica/', views.restorePJuridica.as_view()),

    ]
