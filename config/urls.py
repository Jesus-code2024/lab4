from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración
    path('', include('library.urls')),  # Incluye las URLs de la app 'library'
]