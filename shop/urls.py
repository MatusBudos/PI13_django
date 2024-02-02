from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vypis_produktov, name='produkty'),
    path('users/', views.vypis_uzivatelov, name='uzivatelia'),
    path('categories/', views.vypis_kategorie, name='kategorie'),
    path('orders/', views.vypis_objednavok, name='objednavky'),
    path('categories/<kategoria>/', views.vypis_podla_kategorie, name='kategoria'),
    path('products/<produkt>/', views.vypis_produktu, name='produkt'),
]