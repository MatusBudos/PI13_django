import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from skola.models import *
import random
import csv
from datetime import datetime

filesize = 10643

today = datetime.date.today()



f = open("ULICE.csv", "r", encoding="utf8")
riadky = f.readlines()
studenti = Student.objects.all()
ucitelia = Ucitel.objects.all()


for i in studenti:
    nahodny_riadok = random.choice(riadky)
    ulica, psc, obec = nahodny_riadok.split(";")
    i.ulica = f"{ulica} {random.randint(1,1500)}" 
    i.psc = psc
    i.obec = obec
    i.save()
    
for j in ucitelia:
    nahodny_riadok = random.choice(riadky)
    ulica, psc, obec = nahodny_riadok.split(";")
    j.ulica = f"{ulica} {random.randint(1,1500)}" 
    j.psc = psc
    j.obec = obec
    j.save()