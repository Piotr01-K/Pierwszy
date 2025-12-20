import random
from django.core.management.base import BaseCommand
from faker import Faker
from ogloszenia.models import Article, Category


class Command(BaseCommand):
    help = "Tworzy przykładowe artykuły przy użyciu Faker"

    def handle(self, *args, **options):
        fake = Faker("pl_PL")

        categories = Category.objects.all()

        if not categories.exists():
            self.stdout.write(self.style.ERROR(
                "Brak kategorii! Najpierw dodaj kategorie."
            ))
            return

        for i in range(10):
            Article.objects.create(
                title=fake.sentence(nb_words=5),
                content=fake.text(max_nb_chars=1000),
                category=random.choice(categories),
                is_published=True,
            )

        self.stdout.write(self.style.SUCCESS(
            "Utworzono 10 losowych artykułów!"
        ))
