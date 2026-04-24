from django.contrib import admin
from django.urls import path
from .views import index  # jeśli w tym samym katalogu

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
]