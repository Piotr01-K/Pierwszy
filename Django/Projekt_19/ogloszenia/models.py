from django.db import models

class Ogloszenie(models.Model):
    tytul = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=8, decimal_places=2)
    data_dodania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tytul
    
#  dodałem w ramach Task 3
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name