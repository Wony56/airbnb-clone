from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    help = "This command resets users' avatar"

    def handle(self, *args, **options):
        users = User.objects.filter(login_method=User.LOGIN_EMAIL)

        for user in users:
            user.avatar = None
            user.save()
        
        self.stdout.write(self.style.SUCCESS(f"Reset success!"))