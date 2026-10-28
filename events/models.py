import uuid
from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class EventRegistration(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="registrations"
    )

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    registration_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    registered_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.registration_number:
            year = timezone.now().year
            unique_code = uuid.uuid4().hex[:8].upper()
            self.registration_number = f"YAA-{year}-{unique_code}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.registration_number} - {self.full_name}"