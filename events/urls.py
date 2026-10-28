from django.urls import path
from . import views

urlpatterns = [
    path("", views.event_registration, name="event_registration"),
]
