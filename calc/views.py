from django.shortcuts import render, HttpResponse
from . models import *

def calc(request):
    if request.method == "GET":
        return render(request, "calc/index.html")
    else:
        try: 
            a = float(request.POST["a"])
            b = float(request.POST["b"])
        except:
            vysledok = "Zadaj cisla!"
            return render(request, "calc/index.html", {"vysledok":vysledok})
        operator = request.POST["operator"]
        if operator == "+":
            vysledok = a + b
        elif operator == "-":
            vysledok = a - b
        elif operator == "*":
            vysledok = a * b
        elif operator == "/":
            if b != 0:  
                vysledok = a / b
            else: 
                vysledok = "Nulou sa nedá deliť!"
                return render(request, "calc/index.html", {"vysledok":vysledok, "a":a, "b":b, "operator":operator})
        try:
            priklad_check = Priklad.objects.get(a = a, b = b, operator = operator)
        except:
            priklad = Priklad(
                a = a,
                b = b,
                operator = operator,
                vysledok = round(vysledok, 2),
            )       
            priklad.save()
        return render(request, "calc/index.html", {"vysledok":vysledok, "a":a, "b":b, "operator":operator})
