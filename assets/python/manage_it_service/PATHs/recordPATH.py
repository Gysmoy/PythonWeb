from django.urls import path
from manage_it_service.APIs import recordAPI as views

urlpatterns = [
    path('setRecord/', views.setRecord.as_view()),
    path('getRecords/', views.getRecords.as_view()),
]
