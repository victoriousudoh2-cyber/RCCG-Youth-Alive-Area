import os
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Reset an admin password"

    def handle(self, *args, **kwargs):
        username = os.getenv("RESET_ADMIN_USERNAME")
        password = os.getenv("RESET_ADMIN_PASSWORD")

        if not username or not password:
            raise CommandError("Password reset variables are missing.")

        User = get_user_model()

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError("Admin username was not found.")

        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        self.stdout.write("Admin password reset successfully.")
