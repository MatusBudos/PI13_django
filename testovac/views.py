from django.shortcuts import render
import random
from . models import *
from calc.models import *


def testovac(request):
    maximum = Priklad.objects.count()
    cislo = random.randint(1,maximum)
    priklad = Priklad.objects.get(id = cislo)  
    skore = 0
    high_score = High_score.objects.get(id = 1)
    
    if request.method == "GET":
        return render(request, "testovac/index.html", {"priklad": priklad, "skore":skore, "high_score":high_score})
    
    else:
        try: 
            vysledok = float(request.POST["vysledok"])
        except:
            vysledok = "Zadaj čísla!"
            skore = int(request.POST["skore"]) 
            return render(request, "testovac/index.html", {"vysledok":vysledok, "priklad":priklad, "skore":skore, "high_score":high_score})
        
        skore = int(request.POST["skore"]) 

    if float(request.POST["vysledok"]) == float(request.POST["spravny_vysledok"]):
        vysledok = "Správne!!!"
        skore += 1
        if skore > high_score.score:
            high_score.score = skore
            high_score.save()
        return render(request, "testovac/index.html", {"vysledok":vysledok, "priklad":priklad, "skore":skore, "high_score":high_score})
    
    else:
        vysledok = "Zadal si zlý výsledok, skús ďalší príklad!"
        skore -= 1
        return render(request, "testovac/index.html", {"vysledok":vysledok, "priklad":priklad, "skore":skore, "high_score":high_score})
        
    