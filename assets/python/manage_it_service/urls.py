
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('/', include('profiles_api.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls'))
]
