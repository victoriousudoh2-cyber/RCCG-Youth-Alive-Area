
from django.db import migrations
from datetime import datetime, timezone


def add_powernight_event(apps, schema_editor):
    Event = apps.get_model("events", "Event")

    Event.objects.get_or_create(
        title="HOLYGHOST POWERNIGHT",
        defaults={
            "description": "A NIGHT OF DIVINE REMEMBRANCE",
            "event_date": datetime(
                2026, 10, 30, 21, 0, tzinfo=timezone.utc
            ),
            "venue": "No.36 Essien Road, ikot ekpene LGA",
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            add_powernight_event,
            migrations.RunPython.noop,
        ),
    ]
