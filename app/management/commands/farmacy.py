from django.core.management.base import BaseCommand
from app.loadfarmacy import loadfarmacy


class Command(BaseCommand):
    def handle(self, *args, **options):
        loadfarmacy()

        self.stdout.write('Successfully')