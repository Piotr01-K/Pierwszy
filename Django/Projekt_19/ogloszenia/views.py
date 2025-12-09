from django.shortcuts import render
from .models import Product   # dodane w ramach Task 4 lesson 20

def home_view(request):
    context = {
        'user_name': 'Anna',
        'products': [
            {'name': 'Jabłka', 'price': 3.50},
            {'name': 'Banany', 'price': 5.99},
            {'name': 'Truskawki', 'price': 12.00},
        ]
    }
    return render(request, 'home.html', context)

from django.http import HttpResponse

def info_view(request):
    return HttpResponse("Informacje o stronie")

def rules_view(request):
    return HttpResponse("Regulamin")

# dodane w ramach task 4 lesson 20
def product_list_view(request):
    produkty = Product.objects.all()
    return render(request, 'product_list.html', {'produkty': produkty})

# dodane w ramach task 5 lesson 20
def about_view(request):
    return render(request, 'about.html')
