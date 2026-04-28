from django.contrib import admin
from django.urls import path
from .views import *  # jeśli w tym samym katalogu

urlpatterns = [
    path('', index),
    path('section/<str:dzial>', section),
    path('admin/', admin.site.urls),
    path('submitpost/', submitpost),
    path('post/<int:post_id>', post),
    path('submitreply/<int:post_id>', submitreply),
]