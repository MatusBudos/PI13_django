from django.shortcuts import render
from . models import *


def vypis_kategorie(request):
    kategorie = Category.objects.all().order_by("nazov")
    return render(request, "shop/index.html", {"kategorie":kategorie})

def vypis_uzivatelov(request):
    users = User.objects.all().order_by("priezvisko")
    return render(request, "shop/index.html", {"users":users})

def vypis_produktov(request):
    produkty =  Produkt.objects.all().order_by("nazov")
    kategoria = Category.objects.all().order_by("nazov")
    return render(request, "shop/index.html", {"produkty":produkty, "kategoria": kategoria})

def vypis_objednavok(request):
    orders =  Order.objects.all().order_by("user")
    return render(request, "shop/index.html", {"orders":orders})

def vypis_produktu(request, produkt):
    produkt_obj = Produkt.objects.get(nazov = produkt)
    return render(request, "shop/produkt.html", {"produkt":produkt_obj})

def vypis_podla_kategorie(request, kategoria):
    kategoria_obj = Category.objects.get(nazov = kategoria)
    produkty = Produkt.objects.filter(kategoria_id = kategoria_obj.pk).order_by("nazov")
    return render(request, "shop/kategoria.html", {"kategoria": kategoria, "produkty": produkty })