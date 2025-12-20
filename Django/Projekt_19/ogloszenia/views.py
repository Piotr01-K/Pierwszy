from django.shortcuts import render, get_object_or_404
#   from .models import Product   # dodane w ramach Task 4 lesson 20
from .models import Category   #  dodane w ramach Task 3 Lesson 21
from django.utils import timezone    #  dodane w ramach Task 8 Lesson 21
from .models import Article     #  dodane w ramach Task 8 Lesson 21

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

# dodane w ramach task 3 lesson 21
def categories_list_view(request):
    categories = Category.objects.all()
    return render(request, 'categories_list.html', {'categories': categories})

def category_detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})

def article_list_view(request):
    articles = Article.objects.filter(is_published=True)

    q = request.GET.get('q')
    if q:
        articles = articles.filter(title__icontains=q)

    return render(request, "article_list.html", {
        "articles": articles,
        "now": timezone.now(),
    })