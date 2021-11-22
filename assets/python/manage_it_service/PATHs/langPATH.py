from django.urls import path
from manage_it_service.APIs import langAPI as views

urlpatterns = [
    path('setIdiom/', views.setIdiom.as_view()),
    path('getIdioms/', views.getIdioms.as_view()),
    path('getActiveIdioms/', views.getActiveIdioms.as_view()),
    path('getInactiveIdioms/', views.getInactiveIdioms.as_view()),
    path('updateIdiom/', views.updateIdiom.as_view()),
    path('deleteIdiom/', views.deleteIdiom.as_view()),
    path('restoreIdiom/', views.restoreIdiom.as_view()),
]