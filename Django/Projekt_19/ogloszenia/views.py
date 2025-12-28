from django.shortcuts import render, get_object_or_404
#   from .models import Product   # dodane w ramach Task 4 lesson 20
from .models import Category   #  dodane w ramach Task 3 Lesson 21
from django.utils import timezone    #  dodane w ramach Task 8 Lesson 21
from .models import Article     #  dodane w ramach Task 8 Lesson 21
from django.db.models import Count   # dodane w ramach Task 5 Lesson 22
from .forms import ContactForm
from datetime import timedelta   # dodane w ramach Task 8 Lesson 22
from django.views.generic import ListView   # dodane w ramach Task 9 Lesson 22

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

    #  Pobieram parametr z URL
    #   min_comments = request.GET.get('min_comments')

    #  Jeśli parametr istnieje
    #   if min_comments:
    #    articles = articles.annotate(
    #        comments_count=Count('id')  # na razie symbolicznie
    #    ).filter(
    #        comments_count__gte=min_comments
    #    )'''

    # FILTROWANIE: tylko ostatni tydzień   (dodane w ramach task 8 lesson 22)
    recent = request.GET.get('recent')
    if recent == 'true':
        week_ago = timezone.now() - timedelta(days=7)
        articles = articles.filter(created_at__gte=week_ago)

    return render(request, "article_list.html", {
        "articles": articles,
        "now": timezone.now(),
    })

def blog_entries_view(request, blog_id):
    articles = Article.objects.filter(category_id=blog_id)
    return render(
        request,
        'article_list.html',
        {'articles': articles}
    )

# dodane w ramach task 6 lesson 22
def contact_view(request):
    form = ContactForm()
    return render(request, 'ogloszenia/contact.html', {'form': form})

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    context_object_name = "articles"
    paginate_by = 5
    ordering = ["-created_at"]

def get_queryset(self):
        queryset = Article.objects.filter(is_published=True)

        # filtr tekstowy
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(title__icontains=q)

        # filtr ostatniego tygodnia
        recent = self.request.GET.get('recent')
        if recent == 'true':
            week_ago = timezone.now() - timedelta(days=7)
            queryset = queryset.filter(created_at__gte=week_ago)

        return queryset