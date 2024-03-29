from django.urls import path
from manage_it_service.APIs import usersAPI as views

urlpatterns = [
    path('setUser/', views.setUser.as_view()),
    path('getUsers/', views.getUsers.as_view()),
    path('getActiveUsers/', views.getActiveUsers.as_view()),
    path('getInactiveUsers/', views.getInactiveUsers.as_view()),
    path('updateUserDat/', views.updateUserDat.as_view()),
    path('updateUserCredentials/', views.updateUserCredentials.as_view()),
    path('deleteUser/', views.deleteUser.as_view()),
    path('validateUser/', views.validateUser.as_view()),
]