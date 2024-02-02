from django.db import models
from django.utils import timezone

class Vyrobca(models.Model):
    nazov = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nazov}"

class Category(models.Model):
    nazov = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nazov}"

class User(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.meno} {self.priezvisko}"

class Produkt(models.Model):
    vyrobca = models.ForeignKey(Vyrobca, on_delete=models.SET_NULL, null=True)
    nazov = models.CharField(max_length=50)
    popis = models.TextField()
    kategoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cena = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nazov}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    produkt = models.ForeignKey(Produkt, on_delete=models.SET_NULL, null = True)
    datum = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} {self.produkt} {self.datum}"