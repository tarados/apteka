from django.core.management.base import BaseCommand, CommandError
from app.price_parser import priceTxt


class Command(BaseCommand):
    def handle(self, *args, **options):
        priceTxt()

        self.stdout.write('Successfully')
