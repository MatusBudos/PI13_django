from django.shortcuts import render, HttpResponse
from . models import *
from . forms import *

def vypis_skola(request):
    triedy = Trieda.objects.all().order_by("nazov")
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    studenti = Student.objects.all().order_by("priezvisko")
    kruzky = Kruzok.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {"triedy":triedy, "ucitelia":ucitelia, "studenti":studenti, "kruzky":kruzky})
    

def vypis_studentov(request):
    studenti = Student.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"studenti":studenti})

def vypis_triedy(request):
    triedy = Trieda.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {"triedy":triedy})

def vypis_ucitelov(request):
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {"ucitelia":ucitelia})

def vypis_trieda(request, trieda):
    trieda_obj = Trieda.objects.get(nazov = trieda)
    studenti = Student.objects.filter(trieda_id = trieda_obj.pk).order_by("priezvisko")
    studenti_list = []
    for student in studenti:
        studenti_list.append(student)
    ucitel = Ucitel.objects.get(trieda_id = trieda_obj.pk)
    #return HttpResponse(f"{trieda}<br>{ucitel}<br>{studenti_list}")
    return render(request, "skola/trieda_list.html", {"trieda":trieda, "ucitel":ucitel, "studenti":studenti_list})

def vypis_studenta(request, student):
    student = Student.objects.get(id = student)
    trieda = Trieda.objects.get(nazov = student.trieda)
    triedny_ucitel = Ucitel.objects.get(trieda = trieda.id)
    kruzky = Kruzok.objects.filter(student = student)
    return render(request, "skola/student_detail.html", {"student":student, "triedny_ucitel": triedny_ucitel, "trieda":trieda, "kruzky":kruzky})

def vypis_ucitela(request, ucitel):
    ucitel = Ucitel.objects.get(id = ucitel)
    if ucitel.trieda:
        trieda = Trieda.objects.get(nazov = ucitel.trieda)
    else:
        trieda = "Učiteľ nemá triedu"
    try:
        kruzok = Kruzok.objects.get(ucitel = ucitel.pk)
        return render(request, "skola/ucitel_detail.html", {"ucitel":ucitel, "trieda":trieda, "kruzok":kruzok})
    except:
        return render(request, "skola/ucitel_detail.html", {"ucitel":ucitel, "trieda":trieda})

def vypis_kruzkov(request):
    kruzky = Kruzok.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {"kruzky":kruzky})

def vypis_kruzku(request, kruzok):
    kruzok = Kruzok.objects.get(id = kruzok)
    ucitel = Ucitel.objects.get(kruzok = kruzok)
    studenti = Student.objects.filter(kruzok = kruzok).order_by("priezvisko")
    return render(request, "skola/kruzok_detail.html", {"kruzok":kruzok, "ucitel":ucitel, "studenti":studenti})

def pridaj_uzivatel(request):
    if request.method == "POST":
        uzivatel = Uzivatel(
            meno = request.POST["meno"],
            priezvisko = request.POST["priezvisko"],
            email = request.POST["email"],
            datum = request.POST["datum"],
        )
        uzivatel.save()
        return HttpResponse("OK")
    else:
        return render(request, "skola/pridaj_uzivatel.html")
    
def pridaj_uzivatel2(request):
    if request.method == "POST":
        form = UzivatelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
    else:
        form = UzivatelForm()
