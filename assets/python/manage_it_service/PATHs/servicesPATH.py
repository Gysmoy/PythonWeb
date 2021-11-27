from django.urls import path
from manage_it_service.APIs import servicesAPI as views

urlpatterns = [
    path('setService/', views.setService.as_view()),
    path('getServices/', views.getServices.as_view()),
    path('getActiveServices/', views.getActiveServices.as_view()),
    path('getInactiveServices/', views.getInactiveServices.as_view()),
    path('updateServices/', views.updateServices.as_view()),
    path('deleteServices/', views.deleteServices.as_view()),
    path('restoreServices/', views.restoreServices.as_view()),
]

