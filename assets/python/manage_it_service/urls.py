from django.contrib import admin
from django.urls import path, include
from manage_it_service.PATHs import usersPATH

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(usersPATH)),
]
