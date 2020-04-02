from django.core.management.base import BaseCommand
from app.loadfarmacy import add_email


class Command(BaseCommand):
    def handle(self, *args, **options):
        add_email()

        self.stdout.write('Successfully')