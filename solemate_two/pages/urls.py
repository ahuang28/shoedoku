from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.views import serve
from pages import views
import os

from django.conf import settings
base_dir = settings.BASE_DIR

urlpatterns = [
    path('<button>/', views.change_image, name='change_image'),
]
