from django.core.management.base import BaseCommand
from app.loadfarmacy import deleteFarmacy


class Command(BaseCommand):
    def handle(self, *args, **options):
        deleteFarmacy()

        self.stdout.write('Successfully')