import os

from django.db import migrations
from django.contrib.auth.hashers import make_password


def reset_admin_password(apps, schema_editor):
    username = os.environ.get("RESET_ADMIN_USERNAME")
    password = os.environ.get("RESET_ADMIN_PASSWORD")

    if not username or not password:
        raise RuntimeError("Admin reset environment variables are missing.")

    User = apps.get_model("auth", "User")

    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            "password": make_password(password),
            "is_staff": True,
            "is_superuser": True,
            "is_active": True,
        }
    )

    if not created:
        user.password = make_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0002_member_delete_members"),
    ]

    operations = [
        migrations.RunPython(
            reset_admin_password,
            migrations.RunPython.noop,
        ),
    ]
