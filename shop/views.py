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
    return render(request, "shop/index.html", {"produkty":produkty})

def vypis_objednavok(request):
    orders =  Order.objects.all().order_by("user")
    return render(request, "shop/index.html", {"orders":orders})