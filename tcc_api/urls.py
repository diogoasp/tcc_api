from django.urls import include, path
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('enigma_tempo.urls')),
    path('admin/', admin.site.urls),
]
