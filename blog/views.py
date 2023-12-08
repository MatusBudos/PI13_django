from django.shortcuts import render
from . models import *

def vypis_posty(request):
    posty =  Post.objects.all().order_by("autor")
    return render(request, "blog/index.html", {"posty":posty})

def vypis_autorov(request):
    autori = Autor.objects.all().order_by("priezvisko")
    return render(request, "blog/index.html", {"autori":autori})

def vypis_kategorie(request):
    kategorie = Category.objects.all().order_by("nazov")
    return render(request, "blog/index.html", {"kategorie":kategorie})