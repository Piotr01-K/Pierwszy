from django.shortcuts import render

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

