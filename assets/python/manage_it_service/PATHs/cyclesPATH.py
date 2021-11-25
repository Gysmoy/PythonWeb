from django.urls import path
from manage_it_service.APIs import cyclesAPI as views

urlpatterns = [
    path('setCycle/', views.setCycle.as_view()),
    path('getCycles/', views.getCycles.as_view()),
    path('getActiveCycles/', views.getActiveCycles.as_view()),
    path('getInactiveCycles/', views.getInactiveCycles.as_view()),
    path('updateCycle/', views.updateCycle.as_view()),
    path('deleteCycle/', views.deleteCycle.as_view()),
    path('restoreCycle/', views.restoreCycle.as_view()),
]
