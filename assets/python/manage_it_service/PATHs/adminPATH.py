from django.urls import path
from manage_it_service.APIs import adminAPI as views

urlpatterns = [
    path('query/', views.queryAdmin.as_view()),
    ]