from django.urls import path
from manage_it_service.APIs import subsAPI as views

urlpatterns = [
    path('setSubscription/', views.setSubscription.as_view()),
    path('getSubscriptiones/', views.getSubscriptiones.as_view()),
    path('getActiveSubscription/', views.getActiveSubscription.as_view()),
    path('getInactiveSubscription/', views.getInactiveSubscription.as_view()),
    path('updateSubscription/', views.updateSubscription.as_view()),
    path('deleteSubscription/', views.deleteSubscription.as_view()),
    path('restoreSubscription/', views.restoreSubscription.as_view()),
]