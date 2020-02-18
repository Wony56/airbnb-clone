from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "This command creates superuser"

    def handle(self, *args, **options):
        admin = User.objects.get_or_none(username="ebadmin")
        if not admin:
            User.objects.create_superuser("ebadmin", "kalee7878@gmail.com", "admin1234")
            self.stdout.write(self.style.SUCCESS(f"Superuser created!"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser exists!"))