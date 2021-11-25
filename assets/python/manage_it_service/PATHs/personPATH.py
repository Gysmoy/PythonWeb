from django.urls import path
from manage_it_service.APIs import personAPI as views

urlpatterns = [

    # Persona Natural

    path('setPNatural/', views.setPNatural.as_view()),
    path('getPNaturales/', views.getPNaturales.as_view()),
    path('getActivePNaturales/', views.getActivePNaturales.as_view()),
    path('getInactivePNaturales/', views.getInactivePNaturales.as_view()),
    path('updatePNatural/', views.updatePNatural.as_view()),
    path('deletePNatural/', views.deletePNatural.as_view()),
    path('restorePNatural/', views.restorePNatural.as_view()),

    # Persona Juridica

    path('setPJuridica/', views.setPJuridica.as_view()),
    path('getPJuridicas/', views.getPJuridica.as_view()),
    path('getActivePJuridicas/', views.getActivePJuridica.as_view()),
    path('getInactivePJuridicas/', views.getInactivePJuridica.as_view()),
    path('updatePJuridica/', views.updatePJuridica.as_view()),
    path('deletePJuridica/', views.deletePJuridica.as_view()),
    path('restorePJuridica/', views.restorePJuridica.as_view()),

    ]
