from django.db import models
from django.utils import timezone


class Autor(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    prezyvka = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.prezyvka}"
    
class Category(models.Model):
    nazov = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nazov}"

class Post(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now)
    nadpis = models.CharField(max_length=50)
    text = models.TextField()
    kategoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.autor} {self.nadpis} {self.create_date} {self.text}"
