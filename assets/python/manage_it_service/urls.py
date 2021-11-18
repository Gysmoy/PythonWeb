from django.contrib import admin
from django.urls import path, include
from manage_it_service.PATHs import usersPATH
from manage_it_service.PATHs import servicesPATH
from manage_it_service.PATHs import currencyPATH
from manage_it_service.PATHs import personPATH

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(usersPATH)),
    path('services/', include(servicesPATH)),
    path('persona/', include(personPATH)),
]
