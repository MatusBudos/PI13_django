from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_produktov, name='vypis-produkty'),
    path('users/', views.vypis_uzivatelov, name='vypis-uzivatelov'),
    path('categories/', views.vypis_kategorie, name='vypis-kategorie'),
    path('orders/', views.vypis_objednavok, name='vypis-objednavky'),
]