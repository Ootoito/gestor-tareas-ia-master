from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('<slug:slug>/', views.detalle_proyecto, name='detalle_proyecto'),
]
