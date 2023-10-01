from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("results/", views.results, name="results"),
    path('change_image/<str:button_name>/<str:current_image>/', views.change_image, name='change_image'),
]