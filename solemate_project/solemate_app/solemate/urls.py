from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.views import serve

urlpatterns = [
    path("", views.index, name="index"),
    path("results/", views.results, name="results"),
    path('change_image/<str:button_name>/<str:current_image>/', views.index, name='changed_index'),
]   

if settings.DEBUG:
    urlpatterns += [
        path('solemate_app/assets/<path:path>', serve, {'document_root': 'path/to/your/assets/directory'}),
    ]