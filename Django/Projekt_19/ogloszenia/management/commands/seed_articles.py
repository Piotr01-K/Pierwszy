import random
from django.core.management.base import BaseCommand
from faker import Faker
from ogloszenia.models import Article, Category


class Command(BaseCommand):
    help = "Seeduje bazę artykułami i kategoriami"

    def handle(self, *args, **kwargs):
        fake = Faker('pl_PL')

        # Kategorie
        category_names = [
            'Sport',
            'Technologia',
            'Zdrowie',
            'Edukacja',
            'Lifestyle'
        ]

        categories = []
        for name in category_names:
            category, created = Category.objects.get_or_create(name=name)
            categories.append(category)

        self.stdout.write(f'Utworzono {len(categories)} kategorii')
        
            # Artykuły
        for _ in range(10):
            article = Article.objects.create(
                title=fake.sentence(nb_words=6),
                content=fake.text(max_nb_chars=800),
                is_published=True
            )
            # Losowe kategorie (1–3)
            article.categories.set(
                random.sample(categories, random.randint(1, 3))
            )
        self.stdout.write('Utworzono 10 artykułów z kategoriami')
    
