"""
URL configuration for solemate_two project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.views import serve
from pages import views
import os

from django.conf import settings
base_dir = settings.BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('results/',views.results, name='results'),
    path('index/',include("pages.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path(os.path.join(os.path.dirname(base_dir),"pages/assets/<path:file_path>"),serve, {'document_root': 'assets'}),
    ]
