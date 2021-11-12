from django.urls import path


from profiles_api import views

urlpatterns = [
    path('Home_api/', views.HelloApiView.as_view()),
    path('getUser/', views.getUser.as_view()),
    path('getUsers/', views.getUsers.as_view()),
]