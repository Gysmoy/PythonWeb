from django.urls import path
from django.urls.resolvers import URLPattern

from profiles_api import views

urlpatterns = [
    path('Home_api', views.HelloApiView.as_view()),
]