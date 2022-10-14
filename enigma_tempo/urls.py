from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='page_index'),
    path('cartas/', views.cartas, name='page_cartas'),
    path('cartas/<int:id>', views.getCarta, name='carta'),
    path('upload/', views.upload, name='upload'),

]
