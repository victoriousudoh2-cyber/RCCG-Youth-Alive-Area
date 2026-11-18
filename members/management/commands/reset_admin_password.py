from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = "Create or reset the website admin account"

    def handle(self, *args, **kwargs):
        username = os.getenv("RESET_ADMIN_USERNAME")
        password = os.getenv("RESET_ADMIN_PASSWORD")

        if not username or not password:
            raise CommandError("Password reset variables are missing.")

        User = get_user_model()

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "is_staff": True,
                "is_superuser": True,
                "is_active": True,
            }
        )

        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()

        self.stdout.write(
            self.style.SUCCESS("Admin account created or password reset successfully.")
        )
