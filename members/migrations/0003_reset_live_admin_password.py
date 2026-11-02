import os

from django.db import migrations
from django.contrib.auth.hashers import make_password


def reset_admin_password(apps, schema_editor):
    username = os.environ.get("RESET_ADMIN_USERNAME")
    password = os.environ.get("RESET_ADMIN_PASSWORD")

    if not username or not password:
        raise RuntimeError("Admin reset environment variables are missing.")

    User = apps.get_model("auth", "User")

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise RuntimeError("Admin username was not found.")

    user.password = make_password(password)
    user.is_staff = True
    user.is_superuser = True
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
