from django.contrib import admin
from django.urls import path, include
from manage_it_service.PATHs import usersPATH as users
from manage_it_service.PATHs import servicesPATH as services
from manage_it_service.PATHs import currencyPATH as currency
from manage_it_service.PATHs import personPATH as persona
from manage_it_service.PATHs import adminPATH as admin
from manage_it_service.PATHs import langPATH as lang

urlpatterns = [
    path('admin/', include(admin)),
    path('users/', include(users)),
    path('services/', include(services)),
    path('persona/', include(persona)),
    path('currency/', include(currency)),
    path('lang/', include(lang)),
]
