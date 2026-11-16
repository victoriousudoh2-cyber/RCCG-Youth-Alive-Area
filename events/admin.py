
from django.contrib import admin
from .models import Event, EventRegistration


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date", "venue")


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "gender")

    search_fields = (
        "full_name",
        "email",
        "phone",
        "registration_number",
    )

    readonly_fields = (
        "registration_number",
        "registered_at",
    )
