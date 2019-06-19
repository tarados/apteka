from django.core.management.base import BaseCommand
from app.price_parser import deletePrice


class Command(BaseCommand):
    def handle(self, *args, **options):
        deletePrice()

        self.stdout.write('Successfully')