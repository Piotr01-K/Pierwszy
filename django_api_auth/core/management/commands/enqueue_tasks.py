import random

from django.core.management.base import BaseCommand

from core.tasks import multiply


class Command(BaseCommand):
    help = "Dodaje do kolejki 50 zadań Celery multiply z losowymi argumentami"

    def handle(self, *args, **options):
        for i in range(50):
            a = random.randint(1, 10)
            b = random.randint(1, 10)

            multiply.delay(a, b)

            self.stdout.write(
                self.style.SUCCESS(
                    f"Zadanie {i + 1}: multiply({a}, {b}) dodane do kolejki"
                )
            )
